# from christmas_crowdsource.settings import STRIPE_API_KEY
# from christmas_list.models import Pledge, Item
# from django.shortcuts import render
# from django.views.generic import View
# import stripe
#
#
# class UserCharge(View):
#
#     def get(self, *args, **kwargs):
#         return render(self.request, 'users/donate.html')
#
#     def post(self, *args, **kwargs):
#         stripe.api_key = STRIPE_API_KEY
#
#         # Get the credit card details submitted by the form
#         token = self.request.POST['stripeToken']
#         amount = float(self.request.POST['amount']) * 100
#         amount = int(amount)
#
#         # Create the charge on Stripe's servers - this will charge the user's card
#         try:
#           charge = stripe.Charge.create(
#               amount=amount,
#               currency="usd",
#               source=token,
#               description="Example charge"
#           )
#           item = Item.objects.get(pk=1)
#           Pledge.objects.create(user=self.request.user, amount=amount/100,
#                                 item=item)
#
#         except stripe.error.CardError as e:
#           # The card has been declined
#           pass
#
#         return render(self.request, 'users/donate.html')
