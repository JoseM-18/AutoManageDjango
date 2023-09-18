from django.shortcuts import render, redirect, get_object_or_404
from .models import Car, Order
from .forms import CarForm, OrderForm

def home(request):
    return render(request, 'home.html')

def inventario(request):
    cars = Car.objects.all()
    return render(request, 'inventario.html', {'cars': cars})

def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventario')
    else:
        form = CarForm()
    return render(request, 'add_car.html', {'form': form})

def edit_car(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('inventario')
    else:
        form = CarForm(instance=car)
    return render(request, 'edit_car.html', {'form': form})

def delete_car(request, pk):
    car = get_object_or_404(Car, pk=pk)
    car.delete()
    return redirect('inventario')

def pedido(request):
    orders = Order.objects.all()
    return render(request, 'pedido.html', {'orders': orders})

def add_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pedido')
    else:
        form = OrderForm()
    return render(request, 'add_order.html', {'form': form})

def edit_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('pedido')
    else:
        form = OrderForm(instance=order)
    return render(request, 'edit_order.html', {'form': form})

def delete_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.delete()
    return redirect('pedido')