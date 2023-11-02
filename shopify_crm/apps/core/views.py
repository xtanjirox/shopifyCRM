from django.views import generic
from django.urls import reverse_lazy

from apps.core import models
from apps.core import forms


class HomePage(generic.TemplateView):
    template_name = 'pages/index.html'


class SignIn(generic.TemplateView):
    template_name = 'pages/account/sign-in.html'


class SignUp(generic.TemplateView):
    template_name = 'pages/account/sign-up.html'


class ProductListView(generic.ListView):
    template_name = "pages/product/product-list.html"
    model = models.Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'create_url': reverse_lazy('product-create'),
            'segment': 'product'
        })
        return context


class ProductCreateView(generic.CreateView):
    template_name = "pages/product/product-create.html"
    model = models.Product
    form_class = forms.ProductCreateForm
    success_url = '/product'
