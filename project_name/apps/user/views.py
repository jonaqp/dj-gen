from django.views.generic import TemplateView
from django.utils.translation import ugettext_lazy as _


class IndexView(TemplateView):
    template_name = 'themes/pages/home/home.html'

    def get(self, request, *args, **kwargs):
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text_central"] = _("portal")
        return context
