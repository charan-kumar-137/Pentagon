# Generated by Django 3.0.7 on 2020-07-12 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('date', models.DateField(auto_created=True)),
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='post')),
                ('username', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('total_likes', models.IntegerField(default=0)),
                ('total_comments', models.IntegerField(default=0)),
            ],
        ),
    ]
