from django.db import models


# Create your models here.

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='post')
    username = models.CharField(max_length=30)
    description = models.TextField()
    total_likes = models.IntegerField(default=0)
    total_comments = models.IntegerField(default=0)

    def __int__(self):
        return self.post_id


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    post_id = models.IntegerField()
    description = models.TextField()

    def __int__(self):
        return self.comment_id
