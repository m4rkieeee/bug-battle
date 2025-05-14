from django.contrib import admin
from .models import Training, TrainingSubscription


@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(TrainingSubscription)
class TrainingSubscriptionAdmin(admin.ModelAdmin):
    list_display = ("student", "training", "subscribed", "timestamp")
    list_filter = ("subscribed", "training")
    search_fields = ("student__username", "training__name")
    autocomplete_fields = ("student", "training")
