from django.contrib import admin

from .models import Pin, VectorMap

class PinInline(admin.StackedInline):
    model = Pin
    extra = 1

class VectorMapAdmin(admin.ModelAdmin):
    list_display = ("name",)
    inlines = (PinInline,)

admin.site.register(VectorMap, VectorMapAdmin)
