from django.db import models

# Create your models here.
from wagtail.core.models import Page
from wagtail.core.fields import StreamField, RichTextField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, InlinePanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock

class ChildHomePage(Page):
  body = StreamField([
      ('heading', blocks.CharBlock(classname="full title")),
      ('paragraph', blocks.RichTextBlock()),
      ('image', ImageChooserBlock()),
      ('blockquote', blocks.BlockQuoteBlock()),
      ('embed', EmbedBlock())
  ])

  content_panels = Page.content_panels + [
      StreamFieldPanel('body'),
  ]

class ChildSubPage(Page):
  body = RichTextField(blank=True)

  content_panels = Page.content_panels + [
      FieldPanel('body'),
  ]
