from django.db.models.signals import pre_save
from django.contrib.auth.models import User

def updateUser(sender, instance, **kwargs):
    User = instance
    if User.email != '':
        User.username = User.email


pre_save.connect(updateUser, sender=User)
