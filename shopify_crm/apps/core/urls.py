from apps.core import views
from django.urls import path

urlpatterns = [
    path('', views.HomePage.as_view(), name='index'),

    # Auth urls paths
    path('sign-in', views.SignIn.as_view(), name='sign-in'),
    path('sign-up', views.SignUp.as_view(), name='sign-up'),

    # Product urls paths
    path('product', views.ProductListView.as_view(), name='product-list'),
    path('product/create', views.ProductCreateView.as_view(), name='product-create'),

]
