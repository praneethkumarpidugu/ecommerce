import stripe
from django.conf import settings
from django.contrib.auth.signals import user_logged_in

from .models import UserStripe
stripe.api_key = settings.STRIPE_SECRET_KEY

def get_or_create_stripe(sender, user, *args, **kwargs):
    #print(sender)
    #print(user.email)
    try:
        user.userstripe.stripe_id
    except UserStripe.DoesNotExist:
        customer = stripe.Customer.create(
          email = str(user.email)
        )
        new_user_stripe = UserStripe.objects.create(
            user=user,
            stripe_id=customer.id,
        )
    except:
        pass

#creating a connection to send a signal to receiver function
#say for example get_or_create_stripe
user_logged_in.connect(get_or_create_stripe)