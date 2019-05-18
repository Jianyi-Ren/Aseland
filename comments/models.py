# from django.db import models
# from django.utils import timezone
# from articles.models import Article
# from users.models import CustomUser
#
# class Comment(models.Model):
#     created = models.DateTimeField(default=timezone.now)
#     updated = models.DateTimeField(auto_now=True)
#     author = models.ForeignKey(CustomUser, related_name='comments', on_delete=models.PROTECT)
#
#     article_id = models.ForeignKey(Article, related_name='comments', on_delete=models.PROTECT)
#
#     content = models.TextField(blank=True)
#     fans = models.ManyToManyField(CustomUser)
#
#     def __str__(self):
#         return self.email