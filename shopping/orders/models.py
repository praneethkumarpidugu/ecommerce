from django.db import models

# Create your models here.
from carts.models import Cart

STATUS_CHOICES = (
    ("Started", "Started"),
    ("Abondoned", "Abondoned"),
    ("Finished", "Finished"),
)

class Order(models.Model):
    #add user
    #address **
    #subtotal
    #tax
    #final price
    order_id = models.CharField(max_length=120, default='ABC', unique=True)
    cart = models.ForeignKey(Cart)
    status = models.CharField(max_length=120, choices=STATUS_CHOICES, default="Start")
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.order_id