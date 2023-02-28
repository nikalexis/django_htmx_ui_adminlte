from django_htmx_ui_adminlte.views.welcome import WelcomeOrigin


class ErrorNotFound(WelcomeOrigin):
    template_name = 'django_adminlte_ui/errors/404.html'


class ErrorServer(WelcomeOrigin):
    template_name = 'django_adminlte_ui/errors/500.html'
