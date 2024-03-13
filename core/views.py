from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Category, SubCategory, Product

# Create your views here.
def home(request):
    return render(request, 'core/home.html')


def view_categories(request):
    main_categories = Category.objects.all()
    return render(request, 'core/categories.html', {'main_categories': main_categories})

def view_products_by_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'core/products_by_category.html', {'category': category, 'products': products})

def view_products_by_subcategory(request, subcategory_id):
    subcategory = get_object_or_404(SubCategory, pk=subcategory_id)
    products = Product.objects.filter(category=subcategory.category, subcategory=subcategory)
    return render(request, 'core/products_by_subcategory.html', {'subcategory': subcategory, 'products': products})