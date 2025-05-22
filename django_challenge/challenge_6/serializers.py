from rest_framework import serializers

class InvoiceLineSerializer(serializers.Serializer):
    description = serializers.CharField()
    qty = serializers.IntegerField()
    unitPrice = serializers.FloatField()
    total = serializers.FloatField()

class InvoiceSerializer(serializers.Serializer):
    studentName = serializers.CharField()
    totalAmount = serializers.FloatField()
    taxRate = serializers.FloatField()
    invoiceDate = serializers.DateField(format='%Y-%m-%d')
    currency = serializers.CharField()
    invoiceNumber = serializers.CharField()
    lines = InvoiceLineSerializer(many=True)

    def validate_currency(self, value):
        if value != "EUR":
            raise serializers.ValidationError("Alleen 'EUR' wordt ondersteund.")
        return value

    def validate_totalAmount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Het bedrag moet groter zijn dan 0.")
        return value
