from django.contrib import admin
from .models import Feature
from .models import Available_Date
from .models import Booking

# Register your models here.

admin.site.register(Feature)
admin.site.register(Available_Date)
admin.site.register(Booking)