from django.db import models
from django.utils import timezone
from articles.models import Article
from users.models import CustomUser

class Comment(models.Model):

    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(CustomUser,null=True, related_name='comments', on_delete=models.SET_NULL)

    source_article = models.ForeignKey(Article, related_name='comments', null=True,  on_delete=models.CASCADE)

    content = models.TextField(blank=True)
    liked_user = models.ManyToManyField(CustomUser, blank=True)

    def __str__(self):
        return self.pk