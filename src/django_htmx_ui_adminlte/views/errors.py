from django_htmx_ui_adminlte.views.welcome import WelcomeOrigin


class ErrorNotFound(WelcomeOrigin):
    template_name = 'django_htmx_ui_adminlte/errors/404.html'

    def response_prepare(self, response):
        response = super().response_prepare(response)
        response.status_code = 404
        return response

    def on_get(self, request, *args, **kwargs):
        self.message_warning('404 - Oops, object not found!')

    def on_post(self, request, *args, **kwargs):
        self.message_warning('404 - Oops, object not found!')


class ErrorServer(WelcomeOrigin):
    template_name = 'django_htmx_ui_adminlte/errors/500.html'

    def response_prepare(self, response):
        response = super().response_prepare(response)
        response.status_code = 500
        return response

    def on_get(self, request, *args, **kwargs):
        self.message_error('500 - Oops, server error for that request!')

    def on_post(self, request, *args, **kwargs):
        self.message_error('500 - Oops, server error for that request!')
