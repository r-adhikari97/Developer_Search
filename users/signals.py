# Model import
from .models import Profile
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import  settings

# Signals
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


# Signals
@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.create(
            user=instance,
            username=instance.username,
            email=instance.email,
        )
        print("Profile Created!")

        subject = "Welcome to DevSearch"
        msg = "We are glad to have you!, Here's a Newbie list for you"

        send_mail(
            subject=subject,
            message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[profile.email],
            fail_silently=False
        )


@receiver(post_save, sender=Profile)
def editProfile(sender, instance, created, **kwargs):
    if not created:
        # Disconnect the signal to avoid recursion
        post_save.disconnect(editProfile, sender=Profile)

        user = instance.user
        user.first_name = instance.name
        user.username = instance.username
        user.email = instance.email
        user.save()

        # Reconnect the signal after updating the user
        post_save.connect(editProfile, sender=Profile)


@receiver(post_delete, sender=Profile)
def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()
    print("Deleting User ....")


post_save.connect(createProfile, sender=User)
post_save.connect(editProfile, sender=Profile)
post_delete.connect(deleteUser, sender=Profile)
