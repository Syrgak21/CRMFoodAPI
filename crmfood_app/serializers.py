from rest_framework import serializers
from .models import *


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'


class ServicePercentageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicePercentage
        fields = '__all__'


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class MealToOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealToOrder
        fields = ['mealid', 'count']


class OrderSerializer(serializers.ModelSerializer):
    waiterid = serializers.ReadOnlyField(source='waiterid.id')
    meals = MealToOrderSerializer(many=True)
    tablename = serializers.ReadOnlyField(source='tableid.name')

    class Meta:
        model = Order
        fields = ['id', 'waiterid', 'tableid', 'tablename', 'isitopen', 'date', 'meals']

    def create(self, validated_data):
        meals_data = validated_data.pop('meals')
        order = Order.objects.create(**validated_data)
        for meal_data in meals_data:
            MealToOrder.objects.create(orderid=order, **meal_data)

        return order


class MealToOrderSerializer(serializers.ModelSerializer):
    orderid = serializers.IntegerField(write_only=True)
    meals = MealToOrderSerializer(many=True)

    class Meta:
        model = Order
        fields = ['orderid', 'meals']

    def create(self, validated_data):
        meals_data = validated_data.pop('meals')
        order = Order.objects.get(pk=validated_data['orderid'])
        for meal_data in meals_data:
            MealToOrder.objects.create(orderid=order, **meal_data)
        return order


class CheckSerializer(serializers.ModelSerializer):
    meal = MealToOrderSerializer(many=True, read_only=True, source='orderid__meals')

    class Meta:
        model = Check
        fields = ['id', 'orderid', 'date', 'meal', 'totalSum']


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class MealCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MealCategory
        fields = '__all__'


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = '__all__'
