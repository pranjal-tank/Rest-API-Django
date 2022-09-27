from rest_framework import serializers
from .models import Company,Team

class CompanySerializers(serializers.ModelSerializer):
    class Meta:
        model=Company
        fields=['UUID_company','company_name','company_ceo','company_address','inception_date']

class TeamSerializers(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields=['UUID_team','company_id','team_leader']

class CompanyTeamSerializers(serializers.ModelSerializer):
    teams=TeamSerializers(many=True,read_only=True,source='team_set')
    class Meta:
        model=Company
        fields=['UUID_company','company_name','company_ceo','company_address','inception_date','teams']