from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from users.static import UserConstants

class CustomUser(AbstractUser):
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    name = models.CharField(blank=True, max_length=255)
    status = UserConstants.USER_STATUS_CHOICES
    gender = UserConstants.USER_GENDER_CHOICES

    birthday = models.DateTimeField(default=timezone.now)

    province = models.CharField(blank=True, max_length=255)
    city = models.CharField(blank=True, max_length=255)
    avatar = models.CharField(blank=True, max_length=255)

    sex_acceptance = UserConstants.USER_SEX_ACCEPTANCE_CHOICES
    marriage_status = UserConstants.USER_MARRIAGE_STATUS_CHOICES
    education = UserConstants.USER_EDUCATION_CHOICES

    occupation = models.CharField(blank=True, max_length=255)
    signature = models.CharField(blank=True, max_length=255)

    saved_users = models.ManyToManyField("self", blank=True)
    blocked_users = models.ManyToManyField("self", blank=True)

    def __str__(self):
        return self.email