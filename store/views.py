from django.shortcuts import render


def store(request):
    context = dict()
    return render(request, 'store.html', context)

def card(request):
    context = dict()
    return render(request, 'cart.html', context)

def checkout(request):
    context = dict()
    return render(request, 'checkout.html', context)


