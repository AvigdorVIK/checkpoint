from django.contrib import admin
from .models import *


class SearchAdmin(admin.ModelAdmin):
    list_display = ('title')

admin.site.register(Search)
