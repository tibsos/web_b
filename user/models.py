from django.db import models as m

from django.contrib.auth.models import User

from uuid import uuid4

class UserProfile(m.Model):
    
    uid = m.UUIDField(default = uuid4)
    user = m.OneToOneField(User, on_delete = m.CASCADE)
    
    name = m.TextField()
    
    premium = m.BooleanField(default = False)
    
    premium_since = m.DateTimeField(blank = True, null = True)

    def __str__(self):
        return self.name