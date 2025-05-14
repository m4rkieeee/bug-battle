from django.db import models
from django.contrib.auth.models import User

class Training(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class TrainingSubscription(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    training = models.ForeignKey(Training, related_name="subscriptions", on_delete=models.CASCADE)
    subscribed = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} -> {self.training.name} ({'ingeschreven' if self.subscribed else 'uitgeschreven'})"