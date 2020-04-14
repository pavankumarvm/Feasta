from django.db import models
import uuid

MESS_TYPES = (('Boys', 'Boys'), ('Girls', 'Girls'), ('Both', 'Both'))
FOOD_TYPES = (('Veg', 'Veg'), ('Non-veg', 'Non-veg'),)

class Mess(models.Model):
    """
    Manage all mess menus, and messes
    """
    db_table = "mess"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mess_name = models.CharField(max_length=200, unique=True, blank=False ,null=False)
    longitude = models.CharField(max_length=150, blank=True)
    latitude = models.CharField(max_length=150, blank=True)
    address = models.CharField(max_length=300, blank=False)
    opening_time = models.TimeField(auto_now_add=False, blank=False)
    closing_time = models.TimeField(auto_now_add=False, blank=False)

    # profile_img = models.ImageField(blank=True, null=True)
    rating = models.CharField(max_length=10,default=3)
    review = models.CharField(max_length=1000, blank=True)
    # phone_num = models.CharField(max_length=400)
    # boys or girls or both
    typeof_mess = models.CharField(max_length=10, choices=MESS_TYPES, default=None, blank=False,null=False)
    food_type = models.CharField(max_length=100, choices=FOOD_TYPES, default='Veg', blank=False,null=False)  # veg or non-veg

    one_time = models.IntegerField(blank=False)
    monthly = models.IntegerField(blank=False)

    class Meta:
        unique_together = ('address', 'id')

    def __str__(self):
        return self.mess_name


class Menu(models.Model):
    """
    Store menus from a mess
    """

    db_table = "mess_menu"

    menu_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    item = models.CharField(max_length=200, blank=False)

    # foreign key
    mess_id = models.ForeignKey(Mess, on_delete=models.CASCADE, to_field='id')

    def __str__(self):
        return self.item


class Offer(models.Model):
    """
    Get Offers available
    """
    #Foreign Key Fields
    mess_id = models.ForeignKey(Mess, on_delete=models.CASCADE, to_field='id')
    
    #Key Fields
    item = models.CharField(max_length = 200, blank = False)
    offer = models.PositiveIntegerField()
    item_img = models.FileField(blank = True)
    valid_till = models.DateField(blank = False)
    coupon_code = models.CharField(max_length=30, blank = True)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.item
    # valid_till = models.DateTimeField(default=0)
#
# class Feedback(models.Model):
#     """
#     store rating and review for a mess
#     """
#     mess_id = models.UUIDField()
#     rating = models.IntegerField()
#     review = models.CharField(max_length=500)
#
#     #foreign field to user id
#
