from django.contrib import admin
from .models import Cupom

@admin.register(Cupom)
class CupomAdmin(admin.ModelAdmin):
    list_display = ["titulo"]