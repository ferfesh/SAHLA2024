
from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=100)
    referral_code = models.CharField(max_length=100, unique=True)
    referred_by = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='referrals')

    def __str__(self):
        return self.name

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
