from csv import DictReader
from datetime import datetime

from django.core.management import BaseCommand

from subscriptions.models import Subscription
from pytz import UTC


DATETIME_FORMAT = '%m/%d/%Y %H:%M'


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from subscription_data.csv into our Subscription mode"

    def handle(self, *args, **options):
        if Subscription.objects.exists():
            print('Subscription data already loaded...exiting.')
            return
        print("Loading subscriptions")
        for row in DictReader(open('./subscription_data.csv')):
            subscription = Subscription()
            subscription.category = row['Category']
            subscription.subcategory = row['Subcategory']
            subscription.name = row['Name']
            subscription.plan = row['Plan']
            subscription.price = row['Price']
            subscription.steps = row['Steps']
            subscription.primary_cancellation = row['Primary Cancellation']
            subscription.secondary_cancellation = row['Secondary Cancellation']
            subscription.save()
