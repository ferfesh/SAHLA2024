from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import MemberRegistrationForm
from .models import Member
from rest_framework import viewsets
from .models import Member, Profit, ProfitRate
from .serializers import MemberSerializer, ProfitSerializer, ProfitRateSerializer
from django.contrib.auth.forms import UserCreationForm

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
    if request.method == 'POST':
        form = MemberRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Member.objects.create(
                user=user,
                national_id=form.cleaned_data.get('national_id'),
                phone=form.cleaned_data.get('phone'),
                email=form.cleaned_data.get('email'),
                address=form.cleaned_data.get('address'),
                upline_name=form.cleaned_data.get('upline_name'),
                upline_number=form.cleaned_data.get('upline_number'),
                membership_number=generate_unique_membership_number()
            )
            return redirect('home')
    else:
        form = MemberRegistrationForm()
    return render(request, 'rewards/register.html', {'form': form})
    
"""     if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm() """

def network(request):
    members = Member.objects.all()
    data = []  # بناء البيانات المطلوبة لشجرة الأعضاء هنا
    
    # تحويل بيانات الأعضاء إلى شكل شجرة مناسب
    for member in members:
        data.append({
            "id": member.id,
            "name": member.name,
            "parent_id": member.parent_id,  # افترض أن لديك حقل parent_id لربط الأعضاء
        })
    return render(request, 'rewards/network.html', {'data': data})

