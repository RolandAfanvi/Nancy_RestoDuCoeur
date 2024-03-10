from django.contrib import admin

from authentification_app.models import DistributionSite

# Register your models here.

class AdminDistributionSite(admin.ModelAdmin):
    list_display = ('name', 'address', 'commune')



admin.site.register(DistributionSite,AdminDistributionSite)