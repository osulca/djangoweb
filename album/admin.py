from django.contrib import admin
from .models import Figuras
# Register your models here.@admin.register(Autor)
@admin.register(Figuras)
class FiguraAdmin(admin.ModelAdmin):
	pass
