from django.contrib.auth import get_user_model

from django_htmx_ui_adminlte.views.crud import CrudList

MODEL = get_user_model()
TITLE = 'Users'
ICON = '👤'


class List(CrudListMixin, DefaultPanelOrigin):
    pass
