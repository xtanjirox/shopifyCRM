from apps.core import views
from django.urls import path

urlpatterns = [
    path('', views.HomePage.as_view(), name='index'),
    path('sign-in', views.SignIn.as_view(), name='sign-in'),
    path('sign-up', views.SignUp.as_view(), name='sign-up')
]
