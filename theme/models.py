from django.db import models

class SiteTheme(models.Model):
    bg_color = models.CharField(max_length=20, default="#eaf2ff")
    accent_color = models.CharField(max_length=20, default="#0e5a64")
    text_color = models.CharField(max_length=20, default="#1b2b5a")
    highlight_color = models.CharField(max_length=20, default="#ffc107")
    surface_color = models.CharField(max_length=20, default="#ffffff")

    def __str__(self):
        return "Site Theme"

    class Meta:
        verbose_name = "Site Theme"