from django.db import models

class LessonType(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=100)


class Lesson(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    lesson_type = models.ForeignKey(LessonType, on_delete=models.CASCADE)


class EvaluationQuestion(models.Model):
    text = models.TextField()
    active = models.BooleanField(default=True)
    lesson_type = models.ForeignKey(LessonType, on_delete=models.CASCADE)
