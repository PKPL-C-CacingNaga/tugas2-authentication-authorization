from .models import SiteTheme

def site_theme(request):
    theme, created = SiteTheme.objects.get_or_create(pk=1)
    return {'theme': theme}