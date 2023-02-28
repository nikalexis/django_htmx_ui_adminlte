from django_htmx_ui_adminlte.views.welcome import WelcomeOrigin


class ErrorNotFound(WelcomeOrigin):
    template_name = 'django_htmx_ui_adminlte/errors/404.html'


class ErrorServer(WelcomeOrigin):
    template_name = 'django_htmx_ui_adminlte/errors/500.html'
