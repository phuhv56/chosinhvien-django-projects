#__author__ = 'Der Kaiser'
from datetime import timedelta, datetime
from django.utils.timesince import timesince
from django import template

register = template.Library()

@register.filter(name='age')
def age(value):
    now = datetime.now()
    try:
        difference = now - value
    except:
        return '%(time)s ago ' % {'time': timesince(value).split(', ')[0]}
    if difference <= timedelta(minutes=1):
        return 'just now'

@register.filter(name='get_due_date_string')
def get_due_date_string(value):
    delta = value - datetime.today()

    if delta.days == 0:
        return "Today!"
    elif delta.days < 1:
        return "%s %s ago!" % (abs(delta.days),
            ("day" if abs(delta.days) == 1 else "days"))
    elif delta.days == 1:
        return "Tomorrow"
    elif delta.days > 1:
        return "In %s days" % delta.days