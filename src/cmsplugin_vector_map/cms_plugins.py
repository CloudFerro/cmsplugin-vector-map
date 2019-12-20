from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import VectorMapPlugin
from django.utils.translation import ugettext as _


class VectorMapPluginBase(CMSPluginBase):
    name = _('Vector map')
    model = VectorMapPlugin
    render_template = "cmsplugin_vector_map/_vector_map_plugin.html"
    allow_children = False

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context


plugin_pool.register_plugin(VectorMapPluginBase)
