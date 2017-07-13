from django.contrib import admin
from .models import Order, Topping, Pizza, Address
# Register your models here.


admin.site.register(Order)
admin.site.register(Topping)
admin.site.register(Pizza)
admin.site.register(Address)
