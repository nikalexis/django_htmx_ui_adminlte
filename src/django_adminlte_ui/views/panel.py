from django_adminlte_ui.utils import avatar_url
from django_htmx_ui.utils import ContextProperty
from django_htmx_ui.views.generic import PrivateTemplateView
from django_htmx_ui.views.mixins import PartialMixin


class CommonMixin:

    def response_panel_page(self, url):
        self.response_location(
            url,
            target='#page',
            swap='innerHTML',
        )

    @ContextProperty
    def avatar_url(self):
        return avatar_url(self.request.user)


class PanelPage(CommonMixin, PrivateTemplateView):
    template_root = 'django_adminlte_ui/panel/panel.html'


class PanelPartialPage(CommonMixin, PartialMixin, PrivateTemplateView):
    pass
