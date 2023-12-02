from django.contrib import admin
from .models import Company, Domain

# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    pass


admin.site.register(Company)
admin.site.register(Domain)
