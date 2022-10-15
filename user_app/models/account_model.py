from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from datetime import datetime


# @python_2_unicode_compatible
class Profile(models.Model):
    # id = models.AutoField(primary_key=True, serialize=False)  # phiên bản python 3.9 bắt buộc phải đ/n khóa chính
    # id = models.AutoField(auto_create=True, serialize=False)
    LOCAL_ACCOUNT = 0
    GOOGLE = 1
    FACEBOOK = 2
    LINKEDIN = 3
    SOCIAL_CHOICES = (
        (LOCAL_ACCOUNT, 'Local account'),
        (GOOGLE, 'Google'),
        (FACEBOOK, 'Facebook'),
        (LINKEDIN, 'Linkedin'),
    )
    social_network = models.PositiveSmallIntegerField(choices=SOCIAL_CHOICES, null=True, default=0, blank=True)
    birthday = models.DateField(null=True, default=None, blank=True)
    phone_number = models.CharField(max_length=20, null=True, default=None)
    address = models.CharField(max_length=150, null=True, default=None)
    description = models.CharField(max_length=100, null=True, default=None)
    website = models.URLField(max_length=256, null=True, default=None)
    images = models.ImageField(upload_to='images', null=True, default=None)
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # id table user
    created_at = models.DateTimeField(null=True, default=datetime.now, blank=True)
    updated_at = models.DateTimeField(null=True, default=datetime.now, blank=True)  # auto_now_add=True

    class Meta:
        ordering = ['created_at', 'birthday']
        # managed = True
        db_table = 'profile'
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'

    def __str__(self):
        return self.user.username


# @receiver(post_save, sender=User)
# def create_or_update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     instance.profile.save()

