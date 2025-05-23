from django.contrib import admin
from .models import LessonType, Lesson, EvaluationQuestion, EvaluationStudentAnswer


@admin.register(LessonType)
class LessonTypeAdmin(admin.ModelAdmin):
    list_display = ("code", "name")
    search_fields = ("code", "name")


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("title", "lesson_type", "date")
    list_filter = ("lesson_type", "date")
    search_fields = ("title",)
    date_hierarchy = "date"


@admin.register(EvaluationQuestion)
class EvaluationQuestionAdmin(admin.ModelAdmin):
    list_display = ("text", "lesson_type", "active")
    list_filter = ("lesson_type", "active")
    search_fields = ("text",)

@admin.register(EvaluationStudentAnswer)
class EvaluationStudentAnswerAdmin(admin.ModelAdmin):
    list_display = ("student", "question", "answer")
    list_filter = ("question",)
    search_fields = ("student",)