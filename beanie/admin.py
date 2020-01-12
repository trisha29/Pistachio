from django.contrib import admin

# Register your models here.
from .models import Demographic

class DemographicAdmin(admin.ModelAdmin):
    list_display=('respondent_code','name','sex','contact_number')
    list_filter=('sex','submission_date',)
    list_editable=('contact_number',)
    search_fields=('name','respondent_code',)
    list_per_page=10

admin.site.register(Demographic,DemographicAdmin)

def __str__(self):
    return self.name
