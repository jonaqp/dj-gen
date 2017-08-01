from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'themes/dashboard/base_dashboard.html'

    def get(self, request, *args, **kwargs):
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class UserProfileView(TemplateView):
    template_name = 'themes/pages/user/user_profile.html'

    def get(self, request, *args, **kwargs):
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
