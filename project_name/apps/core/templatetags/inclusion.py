from django import template
from django.db.models import Count
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

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


@register.inclusion_tag('themes/partials/page-breadcrumb.html', takes_context=True)
def tag_menu_breadcrumb(context):
    request = context['request']
    current_language = request.LANGUAGE_CODE
    url_name = request.resolver_match.url_name

    try:
        namespace_name = request.resolver_match.namespaces[0]
        parser = "{0}:{1}".format(str(namespace_name), url_name)
    except IndexError:
        namespace_name = 'index'
        parser = "{0}".format(str(namespace_name))
    url_parse = reverse('{0}'.format(str(parser)))

    crumbs = url_parse.split('/')[2:-1]
    home = _('Home')

    link = u" <li>" \
           u"<i class='icon-home2 position-left'></i>" \
           u"<a href='/{0:s}/'>{1:s}</a>" \
           u"</li>".format(str(current_language), str(home))
    for index, name in enumerate(crumbs):
        link += u"<li class='active'>{0:s}</li>".format(str(name).capitalize())

    return {'result': mark_safe(link)}
