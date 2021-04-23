from django.db import models, IntegrityError
from user.models import User
from django.core.validators import MinValueValidator
from django.conf import settings

class ServicePercentage(models.Model):
  percentage = models.IntegerField(null=False)

  def __str__(self):
      return str(self.percentage)

  class Meta:
    verbose_name_plural = "ServicesPercentage"

  
class Status(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
      return self.name

  class Meta:
    verbose_name_plural = "Statuses"


class Table(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
      return self.name

  class Meta:
    verbose_name_plural = "Tables"
  

class Order(models.Model):
  waiterid = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
  tableid = models.ForeignKey(Table, on_delete=models.CASCADE)
  isitopen = models.BooleanField(default=True)
  date = models.DateTimeField(auto_now_add=True)

  def save(self, *args, **kwargs):
    super(Order, self).save(*args, **kwargs)

  def __str__(self):
      return str(self.id)

  class Meta:
    verbose_name_plural = "Orders"
  
  
class Department(models.Model):
  name = models.CharField(max_length=50, unique=True)

  def __str__(self):
      return self.name

  class Meta:
    verbose_name_plural = "Departments"


class MealCategory(models.Model):
  name = models.CharField(max_length=50, unique=True)
  departmentid = models.ForeignKey(Department, on_delete=models.CASCADE)

  def __str__(self):
      return self.name

  class Meta:
    verbose_name_plural = "MealCategories"
  
  
class Meal(models.Model):
  name = models.CharField(max_length=50)
  categoryid = models.ForeignKey(MealCategory, null=True, on_delete=models.SET_NULL)
  price = models.PositiveIntegerField(validators=[MinValueValidator(1)])
  description = models.TextField(blank=True)

  def __str__(self):
      return self.name

  class Meta:
    verbose_name_plural = "Meals"
  


class MealToOrder(models.Model):
  orderid = models.ForeignKey(Order, related_name='meals', on_delete=models.CASCADE)
  mealid = models.ForeignKey(Meal, related_name='mealsid', on_delete=models.CASCADE)
  count = models.IntegerField()

  def get_total_price(self):
    return self.count * self.mealid.price

  def __str__(self):
      return str(self.orderid.id)

  class Meta:
    verbose_name_plural = "MealsToOrder"



class CheckManager(models.Manager):
  def create_check(self, orderid):
    if not orderid:
      raise IntegrityError("Order is required!")

    orderid.isitopen = False

    prices = [i.get_total_price() for i in orderid.mealid.all()]
    total_sum = sum(prices)

    servicefee = total_sum / 4
    check = self.model(
      orderid=orderid,
      servicefee=servicefee,
      total_sum=total_sum
    )
    check.save()
    return check


class Check(models.Model):
  orderid = models.ForeignKey(Order, related_name='checks', on_delete=models.CASCADE)
  date = models.DateTimeField(auto_now_add=True)
  servicefee = models.IntegerField()
  total_sum = models.IntegerField()

  objects = CheckManager()

  def __str__(self):
      return f"{self.orderid.pk}, Date-{self.date}, Total sum-{self.total_sum}"

  class Meta:
    verbose_name_plural = "Checks"