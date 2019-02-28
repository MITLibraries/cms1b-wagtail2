from django.db import models

# Create your models here.
from wagtail.contrib.settings.models import BaseSetting, register_setting

@register_setting
class SocialMediaSettings(BaseSetting):
    class Meta:
        verbose_name = 'social media accounts'
    facebook = models.URLField(
        help_text='Facebook page URL',
        blank=True
    )
    instagram = models.CharField(
        max_length=255,
        help_text='Instagram username, without the @',
        blank=True
    )
    twitter = models.CharField(
        max_length=255,
        help_text='Your twitter handle without the @',
        blank=True
    )
    youtube = models.URLField(
        help_text='Your YouTube channel or user account URL',
        blank=True
    )

@register_setting
class theme(BaseSetting):
    class Meta:
        verbose_name = 'theme'
    css = models.CharField(
        help_text='theme css',
        max_length=255,
        blank=True
    )
