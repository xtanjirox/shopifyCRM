from django.views import generic


class HomePage(generic.TemplateView):
    template_name = 'pages/index.html'


class SignIn(generic.TemplateView):
    template_name = 'pages/account/sign-in.html'


class SignUp(generic.TemplateView):
    template_name = 'pages/account/sign-up.html'