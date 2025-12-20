from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category, Cart, Order,OrderItem
from Core.models import User

def shop_page(request):
    products = Product.objects.all()
    return render(request, 'Shop/shop.html', {'products': products})


def shop_category(request, category):
    category_obj = get_object_or_404(Category, name__iexact=category)
    products = Product.objects.filter(category=category_obj)
    return render(request, 'Shop/shop.html', {'products': products})


def add_to_cart(request, product_id):
    if not request.session.get('user_id'):
        return redirect('login_page')

    user = User.objects.get(id=request.session['user_id'])
    product = get_object_or_404(Product, id=product_id)

    cart_item, created = Cart.objects.get_or_create(
        user=user,
        product=product
    )

    if not created:
        if cart_item.quantity < product.stock_qty:
            cart_item.quantity += 1
    cart_item.save()

    return redirect('cart_page')


def cart_page(request):
    if not request.session.get('user_id'):
        return redirect('login_page')

    user_id = request.session['user_id']
    cart_items = Cart.objects.filter(user_id=user_id)

    total_amount = 0
    for item in cart_items:
        item.total_price = item.product.price * item.quantity
        total_amount += item.total_price

    return render(request, 'Shop/cart.html', {
        'cart_items': cart_items,
        'total_amount': total_amount
    })

def checkout(request):
    user = User.objects.get(id=request.session['user_id'])
    cart_items = Cart.objects.filter(user=user)

    total = sum(item.product.price * item.quantity for item in cart_items)

    if request.method == 'POST':
        address = request.POST.get('address')

        order = Order.objects.create(
            user=user,
            address=address,
            total_amount=total,
            payment_method="Cash on Delivery"
        )

        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                price=item.product.price,
                quantity=item.quantity
            )

            item.product.stock_qty -= item.quantity
            item.product.save()

        cart_items.delete()

        return redirect('order_success')

    return render(request, 'Shop/checkout.html', {'total': total})


def order_success(request):
    return render(request, 'Shop/order_success.html')

def increase_quantity(request, cart_id):
    cart_item = get_object_or_404(Cart, id=cart_id)

    if cart_item.quantity < cart_item.product.stock_qty:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart_page')


def decrease_quantity(request, cart_id):
    cart_item = get_object_or_404(Cart, id=cart_id)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('cart_page')


def remove_from_cart(request, cart_id):
    cart_item = get_object_or_404(Cart, id=cart_id)
    cart_item.delete()
    return redirect('cart_page')