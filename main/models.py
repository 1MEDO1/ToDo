from django.db import models

# Create your models here.
class ToDo(models.Model):
    text=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    is_closed=models.BooleanField(default=False)
    is_favotite=models.BooleanField(default=False)