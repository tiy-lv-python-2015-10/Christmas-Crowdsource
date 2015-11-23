
import os
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
from christmas_lists.models import Pledge
import stripe


class UserCharge(View):

    def get(self, *args, **kwargs):
        return render(self.request, "users/user_charge.html")


    def post(self, *args, **kwargs):
        stripe.api_key = 'sk_test_biD58COvD5uBeTpom2jHDsjT'
        # stripe.api_key = os.environ['STRIPE_API_KEY']
        token = self.request.POST['stripeToken']

        # Create the charge on Stripe's servers - this will charge the user's card
        try:
            charge = stripe.Charge.create(
            amount=1000, # amount in cents, again
            currency="usd",
            source=token,
            description="Example charge"
        )
            charge_id = charge['id']
        except stripe.error.CardError as e:
            # The card has been declined
            pass





        return render(self.request, "users/user_charge.html")



