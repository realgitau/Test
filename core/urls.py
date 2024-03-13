from django.urls import path, include
from . import views

app_name = 'core'

urlpatterns = [
   path('', views.home, name='home'),
   path('categories/', views.view_categories, name='view_categories'),
   path('category/<int:category_id>/', views.view_products_by_category, name='products_by_category'),
   path('subcategory/<int:subcategory_id>/', views.view_products_by_subcategory, name='products_by_subcategory'),
]