from django.db import models
import uuid

class  Note(models.Model):
    id = models.UUIDField(primary_key = True, 
        default = uuid.uuid4, 
        editable = False)
    title = models.CharField(max_length=250)
    body = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.title 