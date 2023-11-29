import uuid

from django.contrib.auth.models import User as AuthUser
from django.db import models


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(
        AuthUser,
        on_delete=models.CASCADE
    )
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username


class Property(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=True, null=True, default='')
    description = models.TextField()
    location = models.TextField()
    county = models.CharField(max_length=255, blank=True, null=True, default='')
    country = models.CharField(max_length=255, blank=True, null=True, default='')
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=0)
    images = models.ImageField(upload_to=f'houses/{id}')
    listed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'

    def __str__(self):
        return self.name


class RequestViewing(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE
    )
    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE
    )
    preferred_date = models.DateField()
    is_viewed = models.BooleanField(blank=True, null=True, default=False)

    class Meta:
        verbose_name = 'Booked Viewing'
        verbose_name_plural = 'Booked Viewings'



class ContactRequest(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.title
