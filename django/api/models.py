from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

POST_STATUS_CHOICES = (
    ('active', 'active'),
    ('sold', 'sold'),
    ('deleted', 'deleted'),
    ('removed', 'removed'),
)


def get_deleted_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]

class Report(models.Model):
    message = models.TextField(blank=False, null=False)
    post_id = models.IntegerField(default=-1)

class User(AbstractUser):
    phone_number = models.CharField(max_length=30, blank=True, null=True)


class Post(models.Model):
    title = models.TextField(blank=True, null=True, max_length=255)
    body = models.TextField(blank=True, null=True)
    item = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    quality = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    location = models.CharField(max_length=255, blank=True)
    latitude = models.DecimalField(null=True, max_digits=9, decimal_places=6)
    longitude = models.DecimalField(null=True, max_digits=9, decimal_places=6)
    status = models.CharField(max_length=8, choices=POST_STATUS_CHOICES, default='active')
    owner_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='posts',
        on_delete=models.SET(get_deleted_user)
    )
    buyer_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        related_name='items_bought',
        on_delete=models.SET(get_deleted_user)
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Owner: " + str(self.owner_id) +\
               " Title: " + self.title


class Image(models.Model):
    post_id = models.ForeignKey(
        Post,
        related_name='images',
        on_delete=models.CASCADE
    )
    url = models.URLField()


class Messaging(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
        related_name='sent_messages',
        on_delete=models.CASCADE)
    receiver_id = models.ForeignKey(settings.AUTH_USER_MODEL,
        related_name='received_messages',
        on_delete=models.CASCADE)
    post_id = models.ForeignKey('Post',
        related_name='messages',
        on_delete=models.CASCADE)
    parent_message = models.ForeignKey('Messaging',
        related_name='next_message',
        on_delete=models.CASCADE,
        blank=True,
        null=True)
    body = models.TextField(blank=False, max_length=1000)
    date_created = models.DateTimeField(auto_now_add=True)

    # Return a human readable representation of the model instance.
    def __str__(self):
        return "{}".format(self.body)


class PotentialBuyer(models.Model):
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='post_interested_in',
        on_delete=models.CASCADE
    )
    post_id = models.ForeignKey(
        Post,
        related_name = 'potential_buyer',
        on_delete=models.CASCADE
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class BuyerRating(models.Model):
    post_id = models.OneToOneField(
        Post,
        on_delete=models.CASCADE
    )
    rater_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='submitted_buyer_rating',
        on_delete=models.CASCADE
    )
    buyer_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='rating_as_a_buyer',
        on_delete=models.CASCADE
    )
    rating = models.IntegerField(blank=False)
    comment = models.TextField(blank=False,max_length=1000)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class SellerRating(models.Model):
    post_id = models.OneToOneField(
        Post,
        on_delete=models.CASCADE
    )
    rater_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='submitted_seller_rating',
        on_delete=models.CASCADE
    )
    seller_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='rating_as_a_seller',
        on_delete=models.CASCADE
    )
    rating = models.IntegerField(blank=False)
    comment = models.TextField(blank=False,max_length=1000)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

