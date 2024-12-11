from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, CustomerProfile, SellerProfile

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Automatically create profiles based on the user's role.
    """
    if created:
        if instance.role == CustomUser.CUSTOMER:
            CustomerProfile.objects.create(user=instance)
        elif instance.role == CustomUser.SELLER:
            SellerProfile.objects.create(user=instance)
