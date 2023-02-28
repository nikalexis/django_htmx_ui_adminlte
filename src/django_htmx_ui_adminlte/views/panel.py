from django_htmx_ui_adminlte.utils import avatar_url
from django_htmx_ui.utils import ContextProperty
from django_htmx_ui.views.generic import PrivateTemplateView
from django_htmx_ui.views.mixins import PartialTemplateMixin, OriginTemplateMixin


class PanelCommonMixin:

    def response_panel_page(self, url):
        self.response_location(
            str(url),
            target='#page',
            swap='innerHTML',
        )

    @ContextProperty
    def breadcrumb(self):
        breadcrumb = {}
        if hasattr(self, 'instance'):
            if hasattr(self.module, 'List'):
                breadcrumb[self.module.List().title] = self.url(self.module.List)
            breadcrumb[self.instance] = self.url
        else:
            breadcrumb[self.title] = self.url
        return breadcrumb

    @ContextProperty
    def avatar_url(self):
        return avatar_url(self.request.user)


class PanelOrigin(PanelCommonMixin, OriginTemplateMixin, PrivateTemplateView):
    pass


class PanelPartial(PanelCommonMixin, PartialTemplateMixin, PrivateTemplateView):
    pass
