from django.utils.translation import ugettext_lazy as _
from cms.models.pluginmodel import CMSPlugin
from django.db import models
from filer.fields.image import FilerImageField
from djangocms_text_ckeditor.fields import HTMLField
from filer.fields.folder import Folder
from filer.models import ThumbnailOption
from filer.models.imagemodels import Image

class VectorMap(models.Model):
    name = models.CharField(_("Vector map name"), max_length=255)
    VECTOR_MAP_CHOICES = (
        ('world_en', _("World")),
        ('europe_en', _("Europe")),
        ('europe_simple_en', _("Europe (simple)")),
        ('africa_en', _("Africa")),
        ('asia_en', _("Asia")),
        ('australia_en', _("Australia")),
        ('north-america_en', _("North America")),
        ('south-america_en', _("South America")),
    )
    UNIT_CHOICES = (
        ('px', _("pixels (px)")),
        ('%', _("percent (%)")),
        ('em', _("relative to font size (em)")),
    )
    map_type = models.CharField(_("map type"), max_length=255, choices=VECTOR_MAP_CHOICES)
    width = models.PositiveIntegerField(_("width"), null=True, blank=True)
    width_units = models.CharField(_("width units"), max_length=2, choices=UNIT_CHOICES, default='px')
    height = models.PositiveIntegerField(_("height"), null=True, blank=True)
    height_units = models.CharField(_("height units"), max_length=2, choices=UNIT_CHOICES, default='px')

    background_color = models.CharField(_("background color"), max_length=255, blank=True, null=True, help_text=_("Any CSS compatible format"))
    border_color = models.CharField(_("border color"), max_length=255, blank=True, null=True, help_text=_("Any CSS compatible format"))
    border_opacity = models.FloatField(_("border opacity"), default=0.25, help_text=_("In range from 0 to 1"))
    border_width = models.PositiveIntegerField(_("border width"), default=1)
    map_color = models.CharField(_("color of map regions"), max_length=255, blank=True, null=True, help_text=_("Any CSS compatible format"))
    enable_zoom = models.BooleanField(_("enable zoom"), default=True)
    enable_drag = models.BooleanField(_("enable drag"), default=True)
    initial_zoom = models.PositiveIntegerField(_("initial zoom"), default=0)
    hover_color = models.CharField(_("hover color"), max_length=255, blank=True, null=True, help_text=_("Any CSS compatible format"))
    hover_opacity = models.FloatField(_("hover opacity"), default=0.5, help_text=_("In range from 0 to 1"))
    selected_color = models.CharField(_("selected color"), max_length=255, blank=True, null=True, help_text=_("Any CSS compatible format"))
    multi_select_regions = models.BooleanField(_("allow to multi select regions"), default=False)
    show_labels = models.BooleanField(_("Show ISO code labels"), default=False)
    show_tooltip = models.BooleanField(_("Show tooltip on mouseover"), default=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _("Vector map")
        verbose_name_plural = _("Vector maps")

class Pin(models.Model):
    vector_map = models.ForeignKey(VectorMap, verbose_name=_("Vector map"), on_delete=models.CASCADE)
    country_code = models.CharField(_("country code"), max_length=255, blank=True, null=True, help_text=_("Code of the country where the pin will appear"))
    preselect = models.BooleanField(_("preselect region"), default=True)
    text = HTMLField(_("Pin text content"), blank=True, null=True)

    class Meta:
        verbose_name = _("Vector map pin")
        verbose_name_plural = _("Vector map pins")
    

class VectorMapPlugin(CMSPlugin):
    vector_map = models.ForeignKey(VectorMap, verbose_name=_("Choose a vector map"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Vector map add-on")
        verbose_name_plural = ("Vector maps add-ons")
