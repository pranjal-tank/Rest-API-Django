from django.contrib import admin
from .models import Company,Team

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['UUID_company','company_name','company_ceo','company_address','inception_date']

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['UUID_team','company_id','team_leader']