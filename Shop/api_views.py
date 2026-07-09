from django.http import JsonResponse
from .models import Product, Category

def product_list_api(request):
    products = Product.objects.all()

    data = []
    for p in products:
        data.append({
            "id": p.id,
            "name": p.name,
            "price": p.price,
            "stock": p.stock_qty,
            "category": p.category.name,
        })

    return JsonResponse({"products": data})


def category_list_api(request):
    categories = Category.objects.all()

    data = [{"id": c.id, "name": c.name} for c in categories]

    return JsonResponse({"categories": data})
