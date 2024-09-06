from django.contrib import admin
from .models import (
    Foodhub,
    Justeat,
    WTF,
    UberEats,
    Foodhouse,
)



admin.site.register(Foodhub)
admin.site.register(Justeat)
admin.site.register(Foodhouse)
admin.site.register(WTF)
admin.site.register(UberEats)
