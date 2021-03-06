# Generated by Django 2.1.7 on 2019-02-22 22:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMediaSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.URLField(help_text='Facebook page URL')),
                ('instagram', models.CharField(help_text='Instagram username, without the @', max_length=255)),
                ('twitter', models.CharField(help_text='Your twitter handle without the @', max_length=255)),
                ('youtube', models.URLField(help_text='Your YouTube channel or user account URL')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'verbose_name': 'social media accounts',
            },
        ),
    ]
