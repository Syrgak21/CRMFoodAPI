from django.db import models
from user.models import User
from django.core.validators import MinValueValidator

class ServicePercentage(models.Model):
  percentage = models.IntegerField(null=False)

  def __str__(self):
      return str(self.percentage)

  
class Status(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
      return self.name


class Table(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
      return self.name
  

class Order(models.Model):
  waiterid = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
  tableid = models.ForeignKey(Table, on_delete=models.CASCADE)
  isitopen = models.BooleanField(default=True)
  date = models.DateTimeField(auto_now_add=True)

  def save(self, *args, **kwargs):
    super(Order, self).save(*args, **kwargs)

  def __str__(self):
      return str(self.id)
  
  
class Department(models.Model):
  name = models.CharField(max_length=50, unique=True)

  def __str__(self):
      return self.name


class MealCategory(models.Model):
  name = models.CharField(max_length=50, unique=True)
  departmentid = models.ForeignKey(Department, on_delete=models.CASCADE)

  def __str__(self):
      return self.name
  
  
class Meal(models.Model):
  name = models.CharField(max_length=50)
  categoryid = models.ForeignKey(MealCategory, null=True, on_delete=models.SET_NULL)
  price = models.PositiveIntegerField(validators=[MinValueValidator(1)])
  description = models.TextField(blank=True)

  def __str__(self):
      return self.name
  


class MealToOrder(models.Model):
  orderid = models.ForeignKey(Order, related_name='meals', on_delete=models.CASCADE)
  mealid = models.ForeignKey(Meal, related_name='mealsid', on_delete=models.CASCADE)
  count = models.IntegerField()

  def Summ(self):
    return self.count * Meal.objects.get(id=self.meal.id).price

  def __str__(self):
      return str(self.orderid.id)


class Check(models.Model):
  orderid = models.ForeignKey(Order, related_name='checks', on_delete=models.CASCADE)
  date = models.DateTimeField(auto_now_add=True)

  def totalSum(self):
    return sum([i.Summ() for i in MealToOrder.objects.filter(orderid=self.orderid)]) + ServicePercentage.objects.latest('id').percentage

  def __str__(self):
      return str(self.orderid)