from cProfile import label
from sys import maxunicode
from turtle import Turtle
from uuid import UUID
from django.db import models

class Company(models.Model):
    UUID_company = models.AutoField(primary_key=True)
    company_name=models.CharField(max_length=30)
    company_ceo=models.CharField(max_length=40)
    company_address=models.CharField(max_length=50)
    inception_date=models.DateField()

    def __str__(self):
        return str(self.UUID_company)

class Team(models.Model):
    UUID_team=models.AutoField(primary_key=True)
    company_id=models.ForeignKey(Company,on_delete=models.CASCADE)
    team_leader=models.CharField(max_length=40)