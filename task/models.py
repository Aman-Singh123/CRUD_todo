from django.db import models
from datetime import datetime  
class Todo_item(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField(max_length=5000)
    is_done=models.BooleanField(default=False)
    created_at=models.DateTimeField(blank=True,default=datetime.now(),editable=False)
    updated_at=models.DateTimeField(null=True,auto_now=True)