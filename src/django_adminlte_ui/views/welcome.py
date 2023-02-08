from django.contrib.auth import logout, authenticate, login, get_user_model
from django.shortcuts import redirect
from django.urls import reverse
from django_htmx.http import HttpResponseClientRedirect

from django_htmx_ui.views.generic import PublicTemplateView, PrivateTemplateView


class WelcomePage(PublicTemplateView):
    template_root = 'django_adminlte_ui/welcome/welcome.html'


class ErrorNotFound(WelcomePage):
    template_name = 'django_adminlte_ui/errors/404.html'


class ErrorServer(WelcomePage):
    template_name = 'django_adminlte_ui/errors/500.html'


class Logout(PrivateTemplateView):

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse('django_adminlte_ui:login'))


class Login(WelcomePage):
    template_name = 'django_adminlte_ui/welcome/login.html'

    def on_get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse('django_adminlte_ui:dashboard:dashboard'))

    def on_post(self, request, *args, **kwargs):
        user = request.POST['user']
        password = request.POST['password']
        user = authenticate(request, username=user, password=password) or \
            authenticate(request, email=user, password=password)
        if user is not None:
            login(request, user)
        if user and user.is_authenticated:
            return HttpResponseClientRedirect(reverse('django_adminlte_ui:dashboard:dashboard'))
        else:
            self.errors = {'forms': {'login': 'Invalid credentials'}}


class Signup(WelcomePage):
    template_name = 'django_adminlte_ui/welcome/signup.html'

    def on_post(self, request, *args, **kwargs):
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        User = get_user_model()
        if User.objects.filter(email=email).exists():
            self.errors = {'forms': {'signup': 'There is already an account with this email'}}
        elif User.objects.filter(username=email).exists():
            self.errors = {'forms': {'signup': 'There is already an account with this username'}}
        elif password1 != password2:
            self.errors = {'forms': {'signup': 'Passwords do not match each other'}}
        else:
            user = User.objects.create_user(
                username=email,
                email=email,
                password=password1,
            )
            self.add_context('success', True)
