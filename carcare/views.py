from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from .models import Car, Product, Service, Repair, WheelChange, Insurance, Fuel
from .forms import CustomUserCreationForm, CarForm, ServiceForm, RepairForm, WheelChangeForm, InsuranceForm, FuelForm
from .data_layer import CarData


def landing(request):
    return render(request, 'carcare/landing_page.html')

def home(request):
    user_cars = None  # Initialize the variable
    if request.user.is_authenticated:
        user_cars = Car.objects.filter(user=request.user)
    return render(request, 'carcare/home.html', {'user_cars': user_cars})

def cars(request):
    user_cars = None  # Initialize the variable
    if request.user.is_authenticated:
        user_cars = Car.objects.filter(user=request.user)
    return render(request, 'carcare/cars_home.html', {'user_cars': user_cars})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to home page after login
    else:
        form = AuthenticationForm()
    return render(request, 'carcare/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')  # Redirect to home page after logout


def user_register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to home page after registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'carcare/register.html', {'form': form})


@login_required
def create_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            car = form.save(commit=False)
            car.user = request.user
            car.save()
            return redirect('home')
    else:
        form = CarForm()
    return render(request, 'carcare/create.html', {'form': form})

@login_required
def car_details(request, car_id):
    car = get_object_or_404(Car, id=car_id, user=request.user)
    services = Service.objects.filter(car=car)
    repairs = Repair.objects.filter(car=car)
    wheel_changes = WheelChange.objects.filter(car=car)
    insurances = Insurance.objects.filter(car=car)
    fuels = Fuel.objects.filter(car=car)

    service_form = ServiceForm()
    repair_form = RepairForm()
    wheel_change_form = WheelChangeForm()
    insurance_form = InsuranceForm()
    fuel_form = FuelForm()

    return render(request, 'carcare/detail.html', {
        'car': car,
        'services': services,
        'repairs': repairs,
        'wheel_changes': wheel_changes,
        'insurances': insurances,
        'fuels': fuels,
        'service_total_price': sum(service.serv_price for service in services),
        'repair_total_price': sum(repair.repair_price for repair in repairs),
        'wheel_change_total_price': sum(wheel_change.tire_price for wheel_change in wheel_changes),
        'insurance_total_price': sum(insurance.insurance_price for insurance in insurances),
        'fuel_total_price': sum(fuel.fuel_overall_price for fuel in fuels)
        # ... your other context data ...
    })


def service_history(request, car_id):
    car = Car.objects.get(id=car_id)
    services = Service.objects.filter(car=car)
    return render(request, 'carcare/service_history.html', {'car': car, 'services': services})

@login_required
def create_service(request, car_id):
    car = Car.objects.get(id=car_id, user=request.user)

    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            service = form.save(commit=False)
            service.car = car
            service.save()
            return redirect('service_history', car_id=car.id)
    else:
        form = ServiceForm()
    
    return render(request, 'carcare/create_service.html', {'form': form, 'car': car})


def repair_history(request, car_id):
    car = Car.objects.get(id=car_id)
    repairs = Repair.objects.filter(car=car)
    return render(request, 'carcare/repair_history.html', {'car': car, 'repairs': repairs})

@login_required
def create_repair(request, car_id):
    car = Car.objects.get(id=car_id, user=request.user)

    if request.method == 'POST':
        form = RepairForm(request.POST)
        if form.is_valid():
            repair = form.save(commit=False)
            repair.car = car
            repair.save()
            return redirect('car_details', car_id=car.id)
    else:
        form = RepairForm()
    
    return render(request, 'carcare/create_repair.html', {'form': form, 'car': car})


def wheel_change_history(request, car_id):
    car = Car.objects.get(id=car_id)
    wheel_changes = WheelChange.objects.filter(car=car)
    return render(request, 'carcare/wheel_change_history.html', {'car': car, 'wheel_changes': wheel_changes})

@login_required
def create_wheel_change(request, car_id):
    car = Car.objects.get(id=car_id, user=request.user)

    if request.method == 'POST':
        form = WheelChangeForm(request.POST)
        if form.is_valid():
            wheel_change = form.save(commit=False)
            wheel_change.car = car
            wheel_change.save()
            return redirect('car_details', car_id=car.id)
    else:
        form = WheelChangeForm()
    
    return render(request, 'carcare/create_wheel_change.html', {'form': form, 'car': car})


def insurance_history(request, car_id):
    car = Car.objects.get(id=car_id)
    insurances = Insurance.objects.filter(car=car)
    return render(request, 'carcare/insurance_history.html', {'car': car, 'insurances': insurances})

@login_required
def create_insurance(request, car_id):
    car = Car.objects.get(id=car_id, user=request.user)

    if request.method == 'POST':
        form = InsuranceForm(request.POST)
        if form.is_valid():
            insurance = form.save(commit=False)
            insurance.car = car
            insurance.save()
            return redirect('car_details', car_id=car.id)
    else:
        form = InsuranceForm()
    
    return render(request, 'carcare/create_insurance.html', {'form': form, 'car': car})


def fuel_history(request, car_id):
    car = Car.objects.get(id=car_id)
    fuels = Fuel.objects.filter(car=car)
    return render(request, 'carcare/fuel_history.html', {'car': car, 'fuels': fuels})

@login_required
def create_fuel(request, car_id):
    car = Car.objects.get(id=car_id, user=request.user)

    if request.method == 'POST':
        form = FuelForm(request.POST)
        if form.is_valid():
            fuel = form.save(commit=False)
            fuel.car = car
            fuel.save()
            return redirect('car_details', car_id=car.id)
    else:
        form = FuelForm()
    
    return render(request, 'carcare/create_fuel.html', {'form': form, 'car': car})


def about_us(request):
    return render(request, 'carcare/about_us.html')

def contact(request):
    return render(request, 'carcare/contact.html')