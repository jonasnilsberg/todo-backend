from django.db import models

from user.models import User

# Create your models here.

class Task(models.Model):

    RECCURING_CHOICES = (
        (1, "Daily"),
        (2, "Weekly"),
        (3, "Monthly"),
        (4, "Yearly")
    )

    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True)
    recurring = models.BooleanField(default=False)
    reccuring_time = models.CharField(max_length=1, choices=RECCURING_CHOICES, blank=True, null=True)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

