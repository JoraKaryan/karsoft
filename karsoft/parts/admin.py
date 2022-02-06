from django.contrib import admin
from .models import Meals, Reserve, Users, InterfaceControl

admin.site.register(Meals)
admin.site.register(Reserve)
admin.site.register(Users)
admin.site.register(InterfaceControl)