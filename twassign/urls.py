from wsgiref.simple_server import demo_app
from django.contrib import admin
from django.urls import path
from api import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('createcompany',views.CreateCompanyAPI),
    path('getcompany/<int:pk>',views.GetCompanyObjectAPI),
    path('createteam/<int:pk>',views.CreateteamAPI),
    path('allteam/<int:pk>',views.AllTeamAPI),
    path('searchcompany/<str:c>',views.SearchCompanyAPI),
    path('gettoken',TokenObtainPairView.as_view()),
    path('refreshtoken',TokenRefreshView.as_view()),
    path('verifytoken',TokenVerifyView.as_view()),
]
