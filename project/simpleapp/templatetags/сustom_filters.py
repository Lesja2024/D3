from django import template

register = template.Library()

@register.filter(name='censor')
def censor(value):
    bad_words = ['плохое_слово1', 'плохое_слово2']
    for word in bad_words:
        value = value.replace(word, '*' * len(word))
    return value
