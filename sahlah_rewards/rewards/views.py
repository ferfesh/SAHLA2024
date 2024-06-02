from django.shortcuts import render
from rest_framework import viewsets
from .models import Member, Profit, ProfitRate
from .serializers import MemberSerializer, ProfitSerializer, ProfitRateSerializer

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class ProfitViewSet(viewsets.ModelViewSet):
    queryset = Profit.objects.all()
    serializer_class = ProfitSerializer

class ProfitRateViewSet(viewsets.ModelViewSet):
    queryset = ProfitRate.objects.all()
    serializer_class = ProfitRateSerializer

def home(request):
    return render(request, 'rewards/home.html')

def register(request):
    return render(request, 'rewards/register.html')

def network(request):
    return render(request, 'rewards/network.html')
