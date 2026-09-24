from django.contrib import admin

# Register your models here
# from django.contrib import admin
from .models import User, Category, FoodItem, Cart, Order, OrderItem, Feedback

admin.site.register(User)
admin.site.register(Category)
admin.site.register(FoodItem)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Feedback)