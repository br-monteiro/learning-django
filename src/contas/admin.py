from django.contrib import admin
from .models import Category
from .models import Transactions

admin.site.register(Category)
admin.site.register(Transactions)
