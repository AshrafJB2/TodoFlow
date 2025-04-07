from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    PRIORITY_CHOICES = (
        (1, 'low'),
        (2, 'medium'),
        (3, 'high')
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    description = models.TextField()
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=1)
    completed = models.BooleanField(default=False)
    due_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title