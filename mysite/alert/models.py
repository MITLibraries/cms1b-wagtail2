from django.db import models

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.snippets.models import register_snippet

@register_snippet
class Advisory(models.Model):
    text = models.CharField(max_length=255)
    enddate = models.DateField()

    panels = [
        FieldPanel('text'),
        FieldPanel('enddate'),
    ]

    def __str__(self):
        return self.text
