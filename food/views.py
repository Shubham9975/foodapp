from django.shortcuts import render
from .models import Product

def index(request):

    # Creating sample products
    # prod1 = Product()
    # prod1.name="Product 1"
    # prod1.category_name="Category 1"
    # prod1.category_image="category1.jpg"  # Example category image path
    # prod1.image="product-thumb-1.png" # Example product image path
    # prod1.price=100.00
    # prod1.discount_price=80.00
    # prod1.rating=4.5
    # prod1.stock_quantity=10
    #
    # prod2 = Product()
    # prod2.name="Product 2"
    # prod2.category_name="Category 2"
    # prod2.category_image="category2.jpg"
    # prod2.image="product-thumb-2.png"
    # prod2.price=150.00
    # prod2.discount_price=120.00
    # prod2.rating=4.0
    # prod2.stock_quantity=20
    #
    # prod3 = Product()
    # prod3.name = "Product 3"
    # prod3.category_name = "Category 2"
    # prod3.category_image = "category2.jpg"
    # prod3.image = "product-thumb-3.png"
    # prod3.price = 200.00
    # prod3.discount_price = 160.00
    # prod3.rating = 4.0
    # prod3.stock_quantity = 20
    #
    # prod4 = Product()
    # prod4.name = "Product 4"
    # prod4.category_name = "Category 2"
    # prod4.category_image = "category2.jpg"
    # prod4.image = 'product-thumb-7.png'
    # prod4.price = 400.00
    # prod4.discount_price = 300.00
    # prod4.rating = 4.0
    # prod4.stock_quantity = 20
    #
    # prod5 = Product()
    # prod5.name = "Product 5"
    # prod5.category_name = "Category 2"
    # prod5.category_image = "category2.jpg"
    # prod5.image = "product-thumb-6.png"
    # prod5.price = 100.00
    # prod5.discount_price = 70.00
    # prod5.rating = 4.0
    # prod5.stock_quantity = 20
    #
    #
    # products = [prod1, prod2, prod3, prod4, prod5]

    products = Product.objects.all()

    categories = [
        {'image': 'category-thumb-1.jpg', 'name': 'Fruits & Veges'},
        {'image': 'category-thumb-2.jpg', 'name': 'Breads & Sweets'},
        {'image': 'category-thumb-3.jpg', 'name': 'Fruits & Veges'},
        {'image': 'category-thumb-4.jpg', 'name': 'Beverages'},
        {'image': 'category-thumb-5.jpg', 'name': 'Meat Products'},
        {'image': 'category-thumb-6.jpg', 'name': 'Breads'},
        {'image': 'category-thumb-7.jpg', 'name': 'Fruits & Veges'},
        {'image': 'category-thumb-8.jpg', 'name': 'Breads & Sweets'},
        {'image': 'category-thumb-1.jpg', 'name': 'Fruits & Veges'},
        {'image': 'category-thumb-1.jpg', 'name': 'Beverages'},
        {'image': 'category-thumb-1.jpg', 'name': 'Meat Products'},
        {'image': 'category-thumb-1.jpg', 'name': 'Breads'},
    ]
    return render(request, 'index.html', {'categories': categories, 'products': products})
