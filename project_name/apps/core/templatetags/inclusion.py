from django import template
from django.db.models import Count

from project_name.apps.module.models import RoleModule, RoleModuleItem
from project_name.apps.user.models import User

register = template.Library()


@register.inclusion_tag('themes/partials/siderbar-menu.html', takes_context=True)
def tag_menu_siderbar(context):
    """for order need change line 22, 29, 34"""
    request = context['request']
    user = User.objects.get(email=request.user)
    module_team = RoleModule.current.filter(
        role__team__in=user.team.all()
    ).values('module').annotate(dcount=Count('module'))
    result = dict()
    for x in module_team.iterator():
        m_team = RoleModule.current.get(module=x["module"])
        if m_team.module.name not in result.keys():
            result[m_team.module.name] = list()
        add_module_dict = dict(
            module=dict(
                text=m_team.module.name, match=m_team.module.match,
                submodule=dict()
            )
        )
        result[m_team.module.name].append(add_module_dict)
        m_itemteam = RoleModuleItem.current.filter(
            role_module=m_team)
        if m_itemteam.exists():
            for y in m_itemteam:
                dict_sub_menu = result[m_team.module.name][0]['module']['submodule']
                if y.moduleitem.reference not in dict_sub_menu.keys():
                    dict_sub_menu[y.moduleitem.reference] = list()
                add_module_dict = dict(text=y.moduleitem.name,
                                       match=y.moduleitem.match)
                dict_sub_menu[y.moduleitem.reference].append(add_module_dict)
    return {'result': result}
