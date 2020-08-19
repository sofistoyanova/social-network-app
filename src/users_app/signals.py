from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.mail import send_mail


@receiver(pre_save, sender=User)
def send_welcome_email(sender, instance, **kwargs):
    if not User.objects.filter(email=instance.email):
        send_mail(
            'Welcome to the blog',
            'Hi, thank you for registering to our blog',
            'Sofi Admin',
            [instance.email],
            fail_silently=False,
        )
