from django import template
from django.contrib.auth.models import User

register = template.Library()

@register.filter(name="is_banned")
def is_banned(user_id):
    user = User.objects.get(id=user_id)
    return user.groups.filter(name="default").exists() or user.groups.filter(name="mod").exists()