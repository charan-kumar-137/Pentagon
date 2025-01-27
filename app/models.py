from django.db import models


# Create your models here.

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='post')
    uid = models.IntegerField()
    description = models.TextField()
    total_likes = models.IntegerField(default=0)
    total_comments = models.IntegerField(default=0)

    def __int__(self):
        return self.post_id


class PostComment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    uid = models.IntegerField()
    post_id = models.IntegerField()
    description = models.TextField()

    def __int__(self):
        return self.comment_id


class PostLike(models.Model):
    like_id = models.AutoField(primary_key=True)
    post_id = models.IntegerField()
    uid = models.IntegerField()
    liked = models.BooleanField(default=False)

    def __int__(self):
        return self.like_id


class Chat(models.Model):
    cid = models.AutoField(primary_key=True)
    sender_uid = models.IntegerField()
    receiver_uid = models.IntegerField()
    total_messages = models.IntegerField(default=0)

    def __int__(self):
        return self.cid


class ChatMessage(models.Model):
    cmid = models.AutoField(primary_key=True)
    cid = models.IntegerField()
    uid = models.IntegerField()
    message = models.TextField()

    def __int__(self):
        return self.cmid


class User(models.Model):
    uid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    total_likes = models.IntegerField(default=0)
    total_comments = models.IntegerField(default=0)
    total_posts = models.IntegerField(default=0)

    def __int__(self):
        return self.uid
