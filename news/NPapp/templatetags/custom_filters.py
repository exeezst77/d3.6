from django import template


register = template.Library()

censor_list = ['овцы', 'win']
# Регистрируем наш фильтр под именем currency, чтоб Django понимал,
# что это именно фильтр для шаблонов, а не простая функция.
@register.filter()
def censor(value):
   for word in censor_list:
      value = value.replace(word[1:], '*' * len(word[1:]))
   return value


@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
   d = context['request'].GET.copy()
   for k, v in kwargs.items():
       d[k] = v
   return d.urlencode()