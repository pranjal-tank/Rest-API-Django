from concurrent.futures.process import EXTRA_QUEUED_CALLS
from rest_framework.response import Response
from .models import Company,Team
from .serializers import CompanySerializers,TeamSerializers,CompanyTeamSerializers
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['POST'])
def CreateCompanyAPI(request):
    if request.method == "POST":        
        serializer=CompanySerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':"Company created"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def GetCompanyObjectAPI(request,pk):
    company=Company.objects.get(pk=pk)
    serializer=CompanySerializers(company)
    return Response(serializer.data)

@api_view(['GET','POST'])
def CreateteamAPI(request,pk):
    
    if request.method =="GET":
        company=Company.objects.get(pk=pk)
        serializer=CompanySerializers(company)
        return Response(serializer.data)

    if request.method == "POST":
        request.data["company_id"]=pk        
        serializer=TeamSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':"Team created"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def SearchCompanyAPI(request,c):
    company=Company.objects.filter(company_name=c)
    serializer=CompanySerializers(company,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def AllTeamAPI(request,pk):
    company=Company.objects.filter(pk=pk)
    serializer=CompanyTeamSerializers(company,many=True)
    return Response(serializer.data)
 

        
        
    