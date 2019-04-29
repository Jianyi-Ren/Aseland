from django.contrib.auth.models import AbstractUser
from django.db import models
from model_utils import Choices, FieldTracker
from model_utils.fields import (MonitorField, StatusField)
from Users.static import UserConstants

class CustomUser(AbstractUser):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    name = models.CharField(blank=True, max_length=255)
    status = Choices(
        UserConstants.BUILD_ITEM_STATUS_CREATED,
        UserConstants.BUILD_ITEM_STATUS_IN_PROGRESS,
        UserConstants.BUILD_ITEM_STATUS_COMPLETED,
        UserConstants.BUILD_ITEM_STATUS_CANCELED
    )

    gender = Choices(
        UserConstants.USER_GENDER_FEMALE,
        UserConstants.USER_GENDER_MALE
    )
    province = models.CharField(blank=True, max_length=255)
    city = models.CharField(blank=True, max_length=255)
    avatar = models.CharField(blank=True, max_length=255)

    sex_acceptance = Choices(
        UserConstants.USER_SEX_ACCEPTANCE_NO,
        UserConstants.USER_SEX_ACCEPTANCE_RARE,
        UserConstants.USER_SEX_ACCEPTANCE_REGULAR
    )

    marriage_status = Choices(
        UserConstants.USER_MARRIAGE_SINGLE,
        UserConstants.USER_MARRIAGE_BFGB,
        UserConstants.USER_MARRIAGE_MARRIED,
        UserConstants.USER_MARRIAGE_DIVORCED,
        UserConstants.USER_MARRIAGE_WIDOW
    )

    education = Choices(
        UserConstants.USER_EDUCATION_MIDDLE_SCHOOL_AND_BELOW,
        UserConstants.USER_EDUCATION_HIGH_SCHOOL,
        UserConstants.USER_EDUCATION_COLLEGE,
        UserConstants.USER_EDUCATION_MASTER,
        UserConstants.USER_EDUCATION_PHD
    )

    occupation = models.CharField(blank=True, max_length=255)
    signature = models.CharField(blank=True, max_length=255)

    saved_user = models.ForeignKey(
        blocked_users = models.ManyToManyField("self", blank=True)
    )

    blocked_user = models.ForeignKey(
        blocked_users=models.ManyToManyField("self", blank=True)
    )


    def __str__(self):
        return self.email