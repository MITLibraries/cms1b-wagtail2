from django import template
from alert.models import Advisory

register = template.Library()

# Advisory snippets
@register.inclusion_tag('alert/tags/advisorys.html', takes_context=True)
def advisorys(context):
	return {
		'advisorys': Advisory.objects.all(),
		'request': context['request'],
	}
