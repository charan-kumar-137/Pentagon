from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Post)

admin.site.register(models.PostComment)

admin.site.register(models.PostLike)

admin.site.register(models.Chat)

admin.site.register(models.ChatMessage)

admin.site.register(models.User)
