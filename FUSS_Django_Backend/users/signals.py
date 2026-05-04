from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, Organization, Contributor, Recipient

@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_organization:
            Organization.objects.create(user=instance)
        elif instance.is_contributor:
            Contributor.objects.create(user=instance)
            # if solo doctor, default organization
        elif instance.is_recipient:
            Recipient.objects.create(user=instance)
