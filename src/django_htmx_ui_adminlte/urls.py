from django.conf import settings

from django_htmx_ui_adminlte.views import dashboard, welcome, errors
from django_htmx_ui_adminlte.views.errors import ErrorNotFound, ErrorServer
from django_htmx_ui.utils import collect_paths


app_name = 'django_htmx_ui_adminlte'

urlpatterns_errors = [
    collect_paths(errors, app_name),
] if settings.DEBUG else []

urlpatterns = [
    collect_paths(welcome, app_name),
    collect_paths(dashboard, app_name),
] + urlpatterns_errors

handler400 = handler403 = handler404 = ErrorNotFound.as_view()
handler500 = ErrorServer.as_view()
