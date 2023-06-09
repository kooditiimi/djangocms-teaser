# -*- coding: utf-8 -*-

from django.utils.translation import gettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import Teaser


class TeaserPlugin(CMSPluginBase):
    model = Teaser
    name = _("Teaser")
    render_template = "cms/plugins/teaser.html"

    def render(self, context, instance, placeholder):
        if instance.url:
            link = instance.url
        elif instance.page_link:
            link = instance.page_link.get_absolute_url()
        else:
            link = ""

        context.update({
            'object': instance,
            'placeholder': placeholder,
            'link': link
        })
        return context

plugin_pool.register_plugin(TeaserPlugin)
