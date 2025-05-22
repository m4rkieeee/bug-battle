from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import InvoiceSerializer

# Create your views here.
Challenge6BugView = TemplateView.as_view(template_name='challenge_6.html')

class InvoiceSyncView(APIView):
    def post(self, request):
        serializer = InvoiceSerializer(data=request.data)
        if serializer.is_valid():
            return Response({"status": "ok", "message": "Factuur verwerkt"}, status=200)
        return Response(serializer.errors, status=400)
