__author__ = 'sparky'

from django import template

register = template.Library()

@register.inclusion_tag("boots/bootstrap_grid.html", takes_context=True)
def grid(context):
    return {'classes': ['content'], 'content': context.dicts[1]}


@register.inclusion_tag("boots/bootstrap_grid.html", takes_context=True)
def flow_grid(context):

    return {'classes': ['content-flow'], 'content': context.dicts[1]}

