from django.shortcuts import render, get_object_or_404
from .models import Product


def all_products(request):
    """
    View to show all products, including
    sorting and searching queries
    """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_details(request, product_id):
    """
    View to show product detail
    """

    queryset = Product.objects
    product = get_object_or_404(queryset, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
