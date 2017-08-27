from django.contrib import admin
from django.forms import models
from models import Pair

class PairAdmin(admin.ModelAdmin):
    pass

admin.site.register(Pair, PairAdmin)