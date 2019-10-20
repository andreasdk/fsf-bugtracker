from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required

# Cart view
@login_required
def view_cart(request):
    template_name = 'cart/cart.html'
    """A View that renders the cart contents page"""
    return render(request, template_name)

# Add to cart
@login_required
def add_to_cart(request, id):
    """Add a quantity of the specified feature to the cart"""
    quantity = int(request.POST.get('quantity'))
    
    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity      
    else:
        cart[id] = cart.get(id, quantity) 

    request.session['cart'] = cart
    return redirect(reverse('view_all_features'))

# Remove an item from the cart
@login_required
def delete_item(request, id):
    """
    Remove an item from the cart.
    """ 
    if request.method == 'POST':
        item_id = request.POST.get('id')
        cart = request.session.get('cart', {})
        if cart[item_id] > 0:
            cart.pop(item_id)
            request.session['cart'] = cart
    return redirect(reverse('view_cart'))