from django.contrib import admin
from .models import Warehouse, Product, Client, Sale

admin.site.register(Warehouse)
admin.site.register(Product)
admin.site.register(Client)
admin.site.register(Sale)
