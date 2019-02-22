from django.db import models

# Create your models here.
from wagtail.contrib.settings.models import BaseSetting, register_setting

@register_setting
class SocialMediaSettings(BaseSetting):
    class Meta:
        verbose_name = 'social media accounts'
    facebook = models.URLField(
        help_text='Facebook page URL')
    instagram = models.CharField(
        max_length=255, help_text='Instagram username, without the @')
    twitter = models.CharField(
        max_length=255, help_text='Your twitter handle without the @')
    youtube = models.URLField(
        help_text='Your YouTube channel or user account URL')
