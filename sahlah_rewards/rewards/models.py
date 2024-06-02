
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

def generate_membership_number():
    current_year = datetime.now().year % 100  # آخر رقمين من السنة الحالية
    current_month = datetime.now().month      # الشهر الحالي

    last_member = Member.objects.all().order_by('id').last()
    if not last_member:
        new_serial_number = 1
    else:
        last_serial_number = int(last_member.membership_number[6:12])
        new_serial_number = last_serial_number + 1

    new_serial_number_str = '{:06d}'.format(new_serial_number)
    membership_number = f'ST{current_year:02d}{current_month:02d}{new_serial_number_str}'
    
    return membership_number

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)  # تعديل الحقل ليقبل قيم null مؤقتاً
    membership_number = models.CharField(max_length=12, unique=True, null=True, blank=True)  # تعديل الحقل ليقبل قيم null مؤقتاً
    national_id = models.CharField(max_length=20, default='')
    phone = models.CharField(max_length=15, default='')
    email = models.EmailField(default='')
    address = models.TextField(default='')
    upline_name = models.CharField(max_length=100, default='')
    upline_number = models.CharField(max_length=6, default='')
    name = models.CharField(max_length=100)
    referral_code = models.CharField(max_length=100, unique=True, default='')
    referred_by = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='referrals')

    def __str__(self):
        return self.user.username if self.user else 'Unknown'

    def save(self, *args, **kwargs):
        if not self.membership_number:
            self.membership_number = generate_membership_number()
        super().save(*args, **kwargs)


    def generate_membership_number(self):
        return generate_membership_number()


class Profit(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='profits')
    level = models.IntegerField()
    amount = models.FloatField()

    def __str__(self):
        return f'Profit for {self.member.name} at level {self.level}'

class ProfitRate(models.Model):
    level = models.IntegerField(unique=True)
    rate = models.FloatField()

    def __str__(self):
        return f'Profit rate for level {self.level}'

def calculate_profits(member):
    rates = ProfitRate.objects.all()
    profits = []
    for rate in rates:
        level = rate.level
        # افترض أن لديك دالة لحساب عدد الأعضاء في المستوى المعين
        member_count = count_members_at_level(member, level)
        profit_amount = member_count * rate.rate
        profits.append(Profit(member=member, level=level, amount=profit_amount))
    return profits

def count_members_at_level(member, level):
    # مثال على دالة لحساب عدد الأعضاء في مستوى معين
    if level == 1:
        return member.referrals.count()
    # كرر العملية لمستويات أخرى حسب الحاجة
    return 0

