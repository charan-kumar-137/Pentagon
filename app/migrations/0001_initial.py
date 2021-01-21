# Generated by Django 3.1.1 on 2021-01-21 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('sender', models.CharField(max_length=30, unique=True)),
                ('receiver', models.CharField(max_length=30, unique=True)),
                ('total_messages', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('cmid', models.AutoField(primary_key=True, serialize=False)),
                ('cid', models.IntegerField()),
                ('user', models.CharField(max_length=30)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='post')),
                ('username', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('total_likes', models.IntegerField(default=0)),
                ('total_comments', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=30)),
                ('post_id', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PostLike',
            fields=[
                ('like_id', models.AutoField(primary_key=True, serialize=False)),
                ('post_id', models.IntegerField()),
                ('username', models.CharField(max_length=30)),
                ('liked', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('total_likes', models.IntegerField(default=0)),
                ('total_comments', models.IntegerField(default=0)),
                ('total_posts', models.IntegerField(default=0)),
            ],
        ),
    ]
