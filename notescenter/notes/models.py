from django.db import models
from django.conf import settings
# Create your models here.
class Note(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title=models.CharField(max_length=250)
    content=models.TextField(max_length=250)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

def __str__(self):
    return self.user.username -self.title[:10]
