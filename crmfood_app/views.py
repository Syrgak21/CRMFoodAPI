from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions

from .models import *
from .serializers import *


class DepartmentListAPIView(APIView):
  def get(self, request, format = None):
    departments = Department.objects.all()
    serializer = DepartmentSerializer(departments, many = True)
    return Response(serializer.data)
    
  def post(self, request, format = None):
    serializer = DepartmentSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class DepartmentDetailsAPIView(APIView):
  def get_object(self, pk):
    try:
      return Department.objects.get(pk=pk)
    except Department.DoesNotExist:
      raise status.HTTP_404_NOT_FOUND

  def delete(self, request, pk, format=None):
    department = self.get_object(pk)
    department.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)



class MealCategoryListAPIView(APIView):
  def get(self, request, format = None):
    mealcategories = MealCategory.objects.all()
    serializer = MealCategorySerializer(mealcategories, many = True)
    return Response(serializer.data)
    
  def post(self, request, format = None):
    serializer = MealCategorySerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class MealCategoryDetailsAPIView(APIView):
  def get_object(self, pk):
    try:
      return MealCategory.objects.get(pk=pk)
    except MealCategory.DoesNotExist:
      raise status.HTTP_404_NOT_FOUND

  def delete(self, request, pk, format=None):
    mealcategory = self.get_object(pk)
    mealcategory.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)



class MealListAPIView(APIView):
  def get(self, request, format = None):
    meals = Meal.objects.all()
    serializer = DepartmentSerializer(meals, many = True)
    return Response(serializer.data)
    
  def post(self, request, format = None):
    serializer = MealSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class MealDetailsAPIView(APIView):
  def get_object(self, pk):
    try:
      return Meal.objects.get(pk=pk)
    except Meal.DoesNotExist:
      raise status.HTTP_404_NOT_FOUND

  def get(self, request, pk, format=None):
    meal = self.get_object(pk)
    serializer = MealSerializer(meal)
    return Response(serializer.data)

  def put(self, request, pk, format=None):
    meal = self.get_object(pk)
    serializer = MealSerializer(meal, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    meal = self.get_object(pk)
    meal.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)



class CategoriesByDepartmentAPIView(APIView):
  def get(self, request, pk, format = None):
    categories = MealCategory.objects.filter(departmentid = self.kwargs['pk'])
    serializer = DepartmentSerializer(categories, many = True)
    return Response(serializer.data)



class MealsByCategoryAPIView(APIView):
  def get(self, request, pk, format = None):
    meals = Meal.objects.filter(categoryid = self.kwargs['pk'])
    serializer = MealSerializer(meals, many = True)
    return Response(serializer.data)



class TableListAPIView(APIView):
  def get(self, request, format=None):
    tables = Table.objects.all()
    serializer = TableSerializer(tables, many=True)
    return Response(serializer.data)

  def post(self, request, format=None):
    serializer = TableSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TableDetailsAPIView(APIView):
  def get_object(self, pk):
    try:
      return Table.objects.get(pk=pk)
    except Table.DoesNotExist:
      raise status.HTTP_404_NOT_FOUND

  def delete(self, request, pk, format=None):
    table = self.get_object(pk)
    table.delete()
    return Response(status=status.HHTP_204_NO_CONTENT)


class StatusListAPIView(APIView):
  def get(self, request, format=None):
    statuses = Status.objects.all()
    serializer = StatusSerializer(statuses, many=True)
    return Response(serializer.data)

  def post(self, request, format=None):
    serializer = StatusSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StatusDetailsAPIView(APIView):
  def get_object(self, pk):
    try:
      return Status.objects.get(pk=pk)
    except Status.DoesNotExist:
      raise status.HTTP_404_NOT_FOUND

  def delete(self, request, pk, format=None):
    status = self.get_object(pk)
    status.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


class ServicePercentageListAPIView(APIView):
  def get(self, request, format = None):
    servicepercentage = ServicePercentage.objects.all()
    serializer = ServicePercentageSerializer(servicepercentage, many = True)
    return Response(serializer.data)
    
  def post(self, request, format = None):
    serializer = ServicePercentageSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ServicePercentageDetailsAPIView(APIView):
  def get_object(self, pk):
    try:
      return ServicePercentage.objects.get(pk=pk)
    except ServicePercentage.DoesNotExist:
      raise status.HTTP_404_NOT_FOUND

  def delete(self, request, pk, format=None):
    servicepercentage = self.get_object(pk)
    servicepercentage.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


class OrderListAPIView(APIView):
  def get(self, request, format = None):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many = True)
    return Response(serializer.data)
    
  def post(self, request, format = None):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save(waiterid=self.request.user)
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetailsAPIView(APIView):
  def get_object(self, pk):
    try:
      return Order.objects.get(pk=pk)
    except Order.DoesNotExist:
      raise status.HTTP_404_NOT_FOUND

  def delete(self, request, pk, format=None):
    order = self.get_object(pk)
    order.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


class ActiveOrdersAPIView(APIView):
  def get(self, request, format = None):
    orders = Order.objects.filter(isitopen=True)
    serializer = OrderSerializer(orders, many = True)
    return Response(serializer.data)


class MealsToOrderAPIView(APIView):
  def get(self, request, pk, format = None):
    orders = Order.objects.filter(id = self.kwargs['pk'])
    serializer = MealToOrderSerializer(orders, many = True)
    return Response(serializer.data)
    
  def post(self, request, format = None):
    serializer = MealsToOrderSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def get_object(self, pk):
    try:
      return OneMealToOrder.objects.get(pk=pk)
    except OneMealToOrder.DoesNotExist:
      raise status.HTTP_404_NOT_FOUND

  def delete(self, request, pk, format=None):
    oneMeal = self.get_object(pk)
    oneMeal.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


class ChecksListAPIView(APIView):
  def get(self, request, format = None):
    checks = Check.objects.all()
    serializer = CheckSerializer(checks, many = True)
    return Response(serializer.data)
    
  def post(self, request, format = None):
    serializer = CheckSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChecksDetailAPIView(APIView):
  def get(self, request, pk, format=None):
    checks = Check.objects.get(pk=pk)
    serializer = CheckSerializer(checks)
    return Response(serializer.data)

  def delete(self, request, pk, format=None):
    checks = Checks.objects.get(pk=pk)
    checks.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

  def put(self, request, pk, format=None):
    checks = Check.objects.get(pk=pk)
    serializer = serializers.CheckSerializer(checks, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
