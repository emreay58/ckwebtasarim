from django.contrib import admin
from .models import TeklifFormu,ServicesModel
# Register your models here.


@admin.register(ServicesModel)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields={'slug':('title',)}

admin.site.register(TeklifFormu)
