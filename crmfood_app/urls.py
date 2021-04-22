from django.urls import path
from crmfood_app import views

urlpatterns = [
    path('departments/', views.DepartmentListAPIView.as_view(), name = 'DepartmentList'),
    path('departments/<int:pk>/', views.DepartmentDetailsAPIView.as_view(), name = 'DepartmentDetails'),
    path('mealcategories/', views.MealCategoryListAPIView.as_view(), name = 'MealCategoryList'),
    path('mealcategories/<int:pk>/', views.MealCategoryDetailsAPIView.as_view(), name = 'MealCategoryDetails'),
    path('meals/', views.MealListAPIView.as_view(), name = 'MealList'),
    path('meals/<int:pk>', views.MealDetailsAPIView.as_view(), name = 'MealDetails'),
    path('categoriesbydepartment/<int:pk>', views.CategoriesByDepartmentAPIView.as_view(), name = 'CategoriesByDepartment'),
    path('mealsbycategory/<int:pk>', views.MealsByCategoryAPIView.as_view(), name = 'MealsByCategoryView'),

    path('tables/', views.TableListAPIView.as_view(), name = 'TableList'),
    path('tables/<int:pk>/', views.TableDetailsAPIView.as_view(), name = 'TableDetails'),
    path('statuses/', views.StatusListAPIView.as_view(), name = 'StatusList'),
    path('statuses/<int:pk>/', views.StatusDetailsAPIView.as_view(), name = 'StatusDetails'),
    path('servicepercentage/', views.ServicePercentageListAPIView.as_view(), name = 'ServicePercentageList'),
    path('servicepercentage/<int:pk>/', views.ServicePercentageDetailsAPIView.as_view(), name = 'ServicePercentageDetails'),
    path('orders/', views.OrderListAPIView.as_view(), name = 'OrderList'),
    path('orders/<int:pk>', views.OrderDetailsAPIView.as_view(), name = 'OrderDetails'),
    path('activeorders/', views.ActiveOrdersAPIView.as_view(), name = 'ActiveOrders'),
    path('mealstoorder/<int:pk>', views.MealsToOrderAPIView.as_view(), name = 'MealsOfOrder'),
    path('checks/', views.ChecksListAPIView.as_view(), name = 'Checks'),
    path('checks/<int:pk>', views.ChecksDetailAPIView().as_view(), name = 'Checks'),
]