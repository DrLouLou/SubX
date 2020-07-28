from django.shortcuts import render
# from django.http import HttpResponse
from django.http import Http404
# from django.db.models import Q
from .models import Subscription
# from django.core.paginator import Paginator
# from django.views.generic.list import ListView

def home(request):

    search_query = request.GET.get('search', '')

    if search_query:
        subscriptions = Subscription.objects.filter(name__icontains=search_query)
    else:
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
