from django.shortcuts import render

from django.contrib.auth.models import User
from user.models import UserProfile

def overview(request):
    
    total_users = User.objects.all().count()
    total_premium_users = UserProfile.objects.filter(premium = True).count()
    
    revenue_from_premium_users = total_premium_users * 97
    
    c = {}
    
    c['total_users'] = total_users
    c['premium_users'] = total_premium_users
    c['premium_percentage'] = int(total_premium_users / total_users * 100)
    c['revenue'] = revenue_from_premium_users
    
    return render(request, 'overview.html', c)