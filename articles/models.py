# from django.db import models
# from django.utils import timezone
# from users.models import CustomUser
#
# class Article(models.Model):
#     created = models.DateTimeField(default=timezone.now)
#     updated = models.DateTimeField(auto_now=True)
#     author = models.ForeignKey(CustomUser, related_name='articles', on_delete=models.PROTECT)
#
#     content = models.TextField(blank=True)
#     fans = models.ManyToManyField(CustomUser)
#
#     def __str__(self):
#         return self.email