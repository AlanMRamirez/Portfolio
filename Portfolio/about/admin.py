from django.contrib import admin
from .models import InfoAbout
 
# Register your models here.

class InfoAboutAdmin(admin.ModelAdmin):
    readonly_field = ("created", "updated")
    list_display = ('title', 'order')

admin.site.register(InfoAbout, InfoAboutAdmin)
