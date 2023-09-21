import datetime
from django import forms
from .models import Car, Product, Service, Repair, WheelChange, Insurance, Fuel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as lazy


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=20)
    age = forms.IntegerField()
    address = forms.CharField(max_length=100)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = None  # Remove password validation help_text
        self.fields['password2'].help_text = None  # Remove password confirmation help_text

    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        if len(password) < 8:
            raise ValidationError("Password must contain at least 8 characters.")
        return password

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'phone_number', 'age', 'address']




class MonthYearInput(forms.DateInput):
    input_type = 'month'

class MonthYearField(forms.DateField):
    widget = MonthYearInput
    default_error_messages = {
        'invalid': lazy('Enter a valid month and year.'),
    }

    def strptime(self, value, format):
        return datetime.datetime.strptime(value, '%Y-%m')




class CarForm(forms.ModelForm):
    with open('carcare/texts/carcare/brands_list.txt', 'r') as file:
        BRAND_CHOICES = [(brand.strip(), brand.strip()) for brand in file.readlines()]

    with open('carcare/texts/carcare/color_list.txt', 'r') as file:
        COLOR_CHOICES = [(color.strip(), color.strip()) for color in file.readlines()]

    with open('carcare/texts/carcare/type_list.txt', 'r') as file:
        CAR_TYPE_CHOICES = [(car_type.strip(), car_type.strip()) for car_type in file.readlines()]

    brand = forms.ChoiceField(choices=BRAND_CHOICES)
    color = forms.ChoiceField(choices=COLOR_CHOICES)
    car_type = forms.ChoiceField(choices=CAR_TYPE_CHOICES)
    test_date = MonthYearField(label='Test Date:')

    class Meta:
        model = Car
        fields = ['plate_number', 'brand', 'car_type', 'color', 'year', 'km', 'test_date']




class ServiceForm(forms.ModelForm):
    with open('carcare/texts/carcare/serv_type.txt', 'r') as file:
        SERV_TYPE_CHOICES = [(serv_type.strip(), serv_type.strip()) for serv_type in file.readlines()]

    serv_date = MonthYearField(label='Service Date:')
    serv_type = forms.ChoiceField(choices=SERV_TYPE_CHOICES)

    class Meta:
        model = Service
        fields = ['serv_date', 'serv_km', 'serv_type', 'serv_price']




class RepairForm(forms.ModelForm):

    repair_date = MonthYearField(label='Repair Date:')

    class Meta:
        model = Repair
        fields = ['repair_date', 'repaired_parts', 'breakdown_description', 'repair_price']




class WheelChangeForm(forms.ModelForm):
    with open('carcare/texts/carcare/tire_size.txt', 'r') as file:
        TIRE_SIZE_CHOICES = [(size.strip(), size.strip()) for size in file.readlines()]

    tire_date = MonthYearField(label='Tire Replacment Date:')
    tire_size = forms.ChoiceField(choices=TIRE_SIZE_CHOICES)

    class Meta:
        model = WheelChange
        fields = ['tire_date', 'tire_size', 'tire_km', 'tire_price']




class InsuranceForm(forms.ModelForm):
    insurance_start_date = MonthYearField(label='Insurance Start Date:')
    insurance_expiration_date = MonthYearField(label='Insurance Expiration Date:')

    class Meta:
        model = Insurance
        fields = ['insurance_start_date', 'insurance_expiration_date', 'insurance_company', 'insurance_price']




class FuelForm(forms.ModelForm):
    with open('carcare/texts/carcare/fuel_type.txt', 'r') as file:
        FUEL_TYPE_CHOICES = [(fuel_type.strip(), fuel_type.strip()) for fuel_type in file.readlines()]

    with open('carcare/texts/carcare/station_name.txt', 'r') as file:
        STATION_NAME_CHOICES = [(station_name.strip(), station_name.strip()) for station_name in file.readlines()]

    fuel_type = forms.ChoiceField(choices=FUEL_TYPE_CHOICES)
    station_name = forms.ChoiceField(choices=STATION_NAME_CHOICES)
    fuel_date = MonthYearField(label='Fuel Date:')

    class Meta:
        model = Fuel
        fields = ['fuel_type', 'fuel_amount', 'station_name', 'km_per_tank', 'price_per_gallon', 'fuel_overall_price', 'fuel_date']




