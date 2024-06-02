from django.core.management.base import BaseCommand
from rewards.models import Member, generate_membership_number
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Update existing members with unique membership numbers and user'

    def handle(self, *args, **kwargs):
        members = Member.objects.all()
        for member in members:
            if not member.user:
                # قم بتعيين مستخدم افتراضي أو قم بإنشاء مستخدم جديد
                user = User.objects.create(username=f'user_{member.id}')
                member.user = user
            if not member.membership_number:
                member.membership_number = generate_membership_number()
            member.save()
        self.stdout.write(self.style.SUCCESS('Successfully updated members with user and membership numbers'))
