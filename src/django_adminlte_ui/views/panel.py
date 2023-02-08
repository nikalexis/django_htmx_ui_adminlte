from django_adminlte_ui.utils import avatar_url
from django_htmx_ui.utils import ContextProperty
from django_htmx_ui.views.generic import PrivateTemplateView


class PanelPage(PrivateTemplateView):
    template_root = 'django_adminlte_ui/panel/panel.html'

    @ContextProperty
    def avatar_url(self):
        return avatar_url(self.request.user)
