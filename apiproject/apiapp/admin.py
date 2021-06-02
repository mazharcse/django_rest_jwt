from django.contrib import admin

# Register your models here.
from apiapp.models import Country, State, Address

# Register your models here.
admin.site.register(Country)
admin.site.register(State)
admin.site.register(Address)