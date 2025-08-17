from django.db import models
from django.utils import timezone
# django.contrib.auth.models import User

# Create your models here.

class message(models.Model):
    #user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    recipient_name=models.CharField(max_length=20)
    msg_text=models.TextField()
    date_posted=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"To {self.recipient_name}: {self.msg_text[:11]}..."
