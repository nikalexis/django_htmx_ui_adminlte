from django.contrib.auth import get_user_model

from django_adminlte_ui.views.crud import CrudList

MODEL = get_user_model()
TITLE = 'Users'
ICON = '👤'


class List(CrudListMixin, DefaultPanelOrigin):
    pass
