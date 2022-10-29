from django.contrib import admin
from .models import Ant, Feeding, Food

# Register your models here.
admin.site.register(Ant)
admin.site.register(Feeding)
admin.site.register(Food)
