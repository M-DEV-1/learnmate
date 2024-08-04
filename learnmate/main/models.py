from django.db import models
from django.contrib.auth.models import User

class ToDoItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.title