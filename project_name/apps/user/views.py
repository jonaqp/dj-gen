from django.db.models import Count
from django.views.generic import TemplateView

from project_name.apps.module.models import ModuleTeam
from .models import User


class IndexView(TemplateView):
    template_name = 'themes/dashboard/base_dashboard.html'

    def get(self, request, *args, **kwargs):
        user = User.objects.get(email=self.request.user)
        module_team = ModuleTeam.current.filter(
            team__in=user.team.all()
        ).values('module').annotate(dcount=Count('module'))
        print(module_team)
        self.result = dict()
        for x in module_team.iterator():
            m_team = ModuleTeam.current.get(module=x["module"])
            if m_team.module.name not in self.result.keys():
                self.result[m_team.module.order] = list()
            add_module_dict = dict(module=dict(text=m_team.module.name,
                                               match=m_team.module.match,
                                               submodule=dict()))
            self.result[m_team.module.order].append(add_module_dict)
        #
        #     m_itemteam = ModuleItemTeam.current.filter(
        #         module_team=m_team)
        #     print(m_itemteam)
        #     print("---------")
            # if m_itemteam.exists():
            #     for y in m_itemteam:
            #         dict_sub_menu = self.result[m_team.module.order][0]['module']['submodule']
            #
            #         if y.moduleitem.reference not in dict_sub_menu.keys():
            #             dict_sub_menu[y.moduleitem.reference] = list()

                    # add_module_dict = dict(text=y.moduleitem.name,
                    #                        match=y.moduleitem.match)
                    # dict_sub_menu[y.moduleitem.reference].append(add_module_dict)
                    # print(dict_sub_menu)

        # print(self.result)
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
