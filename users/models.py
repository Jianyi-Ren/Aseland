from django.contrib.auth.models import AbstractUser
from django.db import models
from users.static import UserConstants

class CustomUser(AbstractUser):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    name = models.CharField(blank=True, max_length=255)
    status = (
        0, UserConstants.USER_STATUS_CREATED,
        1, UserConstants.USER_STATUS_ACTIVATED,
        2, UserConstants.USER_STATUS_BLOCKED,
        3, UserConstants.USER_STATUS_DELETED
    )

    gender = (
        0, UserConstants.USER_GENDER_FEMALE,
        1, UserConstants.USER_GENDER_MALE
    )
    province = models.CharField(blank=True, max_length=255)
    city = models.CharField(blank=True, max_length=255)
    avatar = models.CharField(blank=True, max_length=255)

    sex_acceptance = (
        0, UserConstants.USER_SEX_ACCEPTANCE_NO,
        1, UserConstants.USER_SEX_ACCEPTANCE_RARE,
        2, UserConstants.USER_SEX_ACCEPTANCE_REGULAR
    )

    marriage_status = (
        0, UserConstants.USER_MARRIAGE_SINGLE,
        1, UserConstants.USER_MARRIAGE_BFGB,
        2, UserConstants.USER_MARRIAGE_MARRIED,
        3, UserConstants.USER_MARRIAGE_DIVORCED,
        4, UserConstants.USER_MARRIAGE_WIDOW
    )

    education = (
        0, UserConstants.USER_EDUCATION_MIDDLE_SCHOOL_AND_BELOW,
        1, UserConstants.USER_EDUCATION_HIGH_SCHOOL,
        2, UserConstants.USER_EDUCATION_COLLEGE,
        3, UserConstants.USER_EDUCATION_MASTER,
        4, UserConstants.USER_EDUCATION_PHD
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