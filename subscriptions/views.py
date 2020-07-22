from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
# from django.models import Q

from .models import Subscription

def home(request):
    subscriptions = Subscription.objects.all()
    return render(request, 'home.html', {
        'subscriptions': subscriptions,
    })

def subscription_detail(request, subscription_id):
    try:
        subscription = Subscription.objects.get(id=subscription_id)
    except Subscription.DoesNotExist:
        raise Http404('Subscription not found.')
    return render(request, 'subscription_detail.html', {
        'subscription': subscription,
    })