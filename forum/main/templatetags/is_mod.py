from django import template
from django.contrib.auth.models import User

register = template.Library()

@register.filter(name="is_mod")
def is_mod(user_id):
    user = User.objects.get(id=user_id)
    return user.groups.filter(name="mod").exists()