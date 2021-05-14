
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

admin.site.register(Order)
admin.site.register(OrderItem)
