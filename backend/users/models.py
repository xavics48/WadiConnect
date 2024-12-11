from django.db import models  # For model definitions
from django.contrib.auth.models import AbstractUser  # For customizing the User model
from django.conf import settings  # For referencing AUTH_USER_MODEL


class CustomUser(AbstractUser):
    CUSTOMER = 'customer'
    SELLER = 'seller'

    ROLE_CHOICES = [
        (CUSTOMER, 'Customer'),
        (SELLER, 'Seller'),
    ]

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=CUSTOMER)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f"{self.email} ({self.role})"


class CustomerProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="customer_profile")
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email


class SellerProfile(models.Model):
    PENDING = 'pending'
    VERIFIED = 'verified'
    REJECTED = 'rejected'

    VERIFICATION_STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (VERIFIED, 'Verified'),
        (REJECTED, 'Rejected'),
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="seller_profile")
    business_name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    business_address = models.TextField()
    phone = models.CharField(max_length=15)
    verification_status = models.CharField(max_length=20, choices=VERIFICATION_STATUS_CHOICES, default=PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.business_name} ({self.user.email})"
