from django import forms
from django.db import models

from modelcluster.fields import ParentalKey, ParentalManyToManyField


from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.snippets.models import register_snippet

# Create your models here.
class LocationIndexPage(Page):

    body = RichTextField(blank=True)

    def get_context(self, request):
        # Set context to be published posts, sorted alphabetically
        context = super().get_context(request)
        featured = LocationPage.objects.child_of(self).live().filter(featured=True).order_by('title')
        # featured = self.get_children().live().filter(locationpage=True).order_by('title')
        locations = LocationPage.objects.child_of(self).live().filter(featured=False).order_by('title')
        context['featured'] = featured
        context['locations'] = locations
        return context

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full")
    ]

class LocationPage(Page):

    open24x7 = models.BooleanField("Open 24x7",null=False,default=False)
    body = RichTextField(blank=True)
    featured = models.BooleanField("Featured location",null=False,default=False)
    study = models.BooleanField("Has study spaces",null=False,default=False)
    telephone = models.CharField("Telephone",max_length=12)
    academics = ParentalManyToManyField ('location.AcademicField', blank=True)
    # These will need to be grouped into a map picker at some point.
    latitude = models.DecimalField("Latitude",max_digits=9, decimal_places=6, default=42.359220)
    longitude = models.DecimalField("Latitude",max_digits=9, decimal_places=6, default=-71.089354)

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    search_fields = Page.search_fields + [
        index.SearchField('body'),
        index.SearchField('featured'),
        index.SearchField('study'),
        index.SearchField('open24x7'),
        index.SearchField('telephone')
    ]

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        FieldPanel('featured'),
        FieldPanel('study'),
        FieldPanel('open24x7'),
        FieldPanel('telephone'),
        MultiFieldPanel([
            FieldPanel('latitude'),
            FieldPanel('longitude'),
        ], heading="Location"),
        InlinePanel('gallery_images', label="Gallery images"),
        FieldPanel('academics', widget=forms.CheckboxSelectMultiple),
    ]

class LocationGalleryImage(Orderable):
    page = ParentalKey(LocationPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]

@register_snippet
class AcademicField(models.Model):
    name = models.CharField(max_length=255)

    panels = [
        FieldPanel('name'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'academic fields'
