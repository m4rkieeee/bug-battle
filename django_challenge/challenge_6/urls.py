from django.urls import path

from challenge_6.views import Challenge6BugView, InvoiceSyncView

urlpatterns = [
    path('', Challenge6BugView, name='challenge_6'),
    path('api/sync-invoice/', InvoiceSyncView.as_view(), name='invoice-sync'),
]
