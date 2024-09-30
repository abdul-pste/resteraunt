from django.shortcuts import render, redirect

def home(request):
    return render(request, '../templates/base.html')

def main(request):
    return render(request, '../templates/main.html')

def order(request):
    daily_special = {
        'name': 'Shoyu Ramen',
        'price': '11.99',
        'description': 'A classic soy sauce-based broth with soft boiled egg, seaweed, and Chashu.'
    }
    
    context = {
        'daily_special': daily_special
    }
    
    return render(request, '../templates/order.html', context)

def submit_order(request):
    if request.method == 'POST':
        # Collect order items from the form submission
        order_items = []
        if request.POST.get('item_1'):
            order_items.append('Miso Ramen')
        if request.POST.get('item_2'):
            order_items.append('Tonkotsu Ramen')
        if request.POST.get('item_3'):
            order_items.append('Spicy Ramen')
        if request.POST.get('item_4'):
            order_items.append(request.POST.get('item_4'))  # Daily Special

        # Collect extras
        extras = []
        if request.POST.get('topping_chashu'):
            extras.append('Extra Chashu')
        if request.POST.get('topping_egg'):
            extras.append('Soft Boiled Egg')

        # Special instructions
        special_instructions = request.POST.get('special_instructions')

        # Customer information
        customer_name = request.POST.get('name')
        customer_phone = request.POST.get('phone')
        customer_email = request.POST.get('email')

        # Prepare context for the confirmation page
        context = {
            'order_items': order_items,
            'extras': extras,
            'special_instructions': special_instructions,
            'customer_name': customer_name,
            'customer_phone': customer_phone,
            'customer_email': customer_email,
        }

        # Redirect to the confirmation page with the order details
        return render(request, 'confirmation.html', context)

    else:
        # If not a POST request, redirect to the order page
        return redirect('order')
