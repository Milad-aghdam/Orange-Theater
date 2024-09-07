from django.contrib import admin
from .models import (
    Foodhub,
    Justeat,
    WhatTheFork,
    UberEats,
    Foodhouse,
)



admin.site.register(Foodhub)
admin.site.register(Justeat)
admin.site.register(Foodhouse)
admin.site.register(WhatTheFork)
admin.site.register(UberEats)
