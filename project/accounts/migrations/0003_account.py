# Generated by Django 3.2.7 on 2021-09-06 08:02

import accounts.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('api', '0040_delete_invitation'),
        ('accounts', '0002_alter_user_first_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=63)),
                ('last_name', models.CharField(max_length=63)),
                ('about_me', models.CharField(blank=True, max_length=511)),
                ('is_verified', models.BooleanField(default=False)),
                ('full_account', models.BooleanField(default=False)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to=accounts.models.PathAndRename(''))),
                ('profile_image_thumb', models.ImageField(blank=True, null=True, upload_to=accounts.models.PathAndRename(''))),
                ('categories', models.ManyToManyField(related_name='user_categories', to='api.Category')),
                ('followers', models.ManyToManyField(related_name='follower', to='accounts.Account')),
                ('following', models.ManyToManyField(related_name='followings', to='accounts.Account')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]