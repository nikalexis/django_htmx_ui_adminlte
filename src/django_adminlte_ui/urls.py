from django.urls import path

from django_adminlte_ui.views import dashboard
from django_adminlte_ui.views.welcome import Login, Signup, Logout, ErrorNotFound, ErrorServer
from django_htmx_ui.utils import collect_paths


app_name = 'django_adminlte_ui'
urlpatterns = [
    path('', Login.as_view(), name='login'),
    path('signup/', Signup.as_view(), name='signup'),
    path('logout/', Logout.as_view(), name='logout'),
    path('errors/404/', ErrorNotFound.as_view()),
    path('errors/500/', ErrorServer.as_view()),
    collect_paths(dashboard, app_name),
]

handler400 = handler403 = handler404 = ErrorNotFound.as_view()
handler500 = ErrorServer.as_view()
