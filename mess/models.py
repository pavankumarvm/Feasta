from django.db import models
import uuid


class Mess(models.Model):
    """
    Manage all mess menus, and messes
    """
    db_table = "mess"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mess_name = models.CharField(max_length=200, null=False)
    timing = models.TimeField(auto_now_add=False, blank=False)
    # start_end_timing = models.TimeField(auto_now_add=False, blank=False)
    longitude = models.CharField(max_length=150, blank=True)
    latitude = models.CharField(max_length=150, blank=True)
    address = models.CharField(max_length=300, blank=False)

    profile_img = models.FileField(blank=True)
    rating = models.CharField(max_length=10)
    review = models.CharField(max_length=1000, blank=True)
    phone_num = models.CharField(max_length=400)
    type = models.CharField(max_length=100)  # veg or non-veg

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
    offer = models.CharField(max_length=100)
    offer_img = models.FileField()
    coupon_code = models.CharField(max_length=30)
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
