from django import forms
from django.conf import settings
from django.contrib.auth import logout, authenticate, login, get_user_model

from django_htmx_ui.views.crud import FormMixin
from django_htmx_ui.views.generic import PublicTemplateView, PrivateTemplateView
from django_htmx_ui.views.mixins import OriginTemplateMixin

User = get_user_model()

PATH_ROOT = ''


class WelcomeOrigin(OriginTemplateMixin, PublicTemplateView):
    pass


class Root(PublicTemplateView):

    @classmethod
    @property
    def path_route(cls):
        return ''

    def on_get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return self.redirect(
                settings.LOGIN_REDIRECT_URL
            )
        else:
            return self.redirect(
                settings.LOGIN_URL,
            )


class Logout(PrivateTemplateView):

    def on_get(self, request, *args, **kwargs):
        logout(request)
        return self.redirect(
            self.request.GET.get('next') or getattr(settings, 'LOGIN_URL', None) or '/'
        )


class Login(FormMixin, WelcomeOrigin):

    class Form(forms.Form):
        user = forms.CharField()
        password = forms.CharField()

    def authenticate(self, user, password):
        user = authenticate(self.request, username=user, password=password) or \
               authenticate(self.request, email=user, password=password)
        return user

    def on_get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return self.redirect(
                self.request.GET.get('next') or settings.LOGIN_REDIRECT_URL
            )

    def on_post(self, request, *args, **kwargs):
        if self.form.is_valid():
            user = self.authenticate(self.form.cleaned_data.get('user'), self.form.cleaned_data.get('password'))
            if user is not None:
                login(request, user)
            if user and user.is_authenticated:
                return self.redirect(
                    self.request.GET.get('next') or settings.LOGIN_REDIRECT_URL
                )
            else:
                self.form.add_error(None, 'Invalid credentials.')


class Signup(FormMixin, WelcomeOrigin):

    class Form(forms.Form):
        email = forms.EmailField()
        password = forms.CharField()
        confirm_password = forms.CharField()

        def clean(self):
            email = self.cleaned_data.get('email')
            password = self.cleaned_data.get('password')
            confirm_password = self.cleaned_data.get('confirm_password')

            if password != confirm_password:
                self.add_error('password', 'Passwords do not match.')
                return

            if User.objects.filter(username=email).count() > 0:
                self.add_error('email', 'There is already an account with this email.')
                return

            return self.cleaned_data

    def create_user(self):
        user = User(
            username=self.form.cleaned_data.get('email'),
            email=self.form.cleaned_data.get('email'),
            password=self.form.cleaned_data.get('password'),
        )
        user.save()
        return user

    def on_post(self, request, *args, **kwargs):
        if self.form.is_valid():
            self.create_user()
            self.add_context('success', True)
