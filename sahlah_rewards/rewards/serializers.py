from rest_framework import serializers
from .models import Member, Profit, ProfitRate

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

class ProfitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profit
        fields = '__all__'

class ProfitRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfitRate
        fields = '__all__'
