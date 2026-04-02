from django.shortcuts import render, redirect
from .models import SiteTheme
from .forms import SiteThemeForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied




@login_required
def theme_settings(request):
    WHITELIST_EMAILS = [
        'a.anggara.bayuadji.p@gmail.com',
        'aaronsuhaendi@gmail.com',
        'rizkyantariksa02@gmail.com',
        'samuelindriano@gmail.com',
        'wildanhidayatirl@gmail.com',
    ]
    
    if request.user.email not in WHITELIST_EMAILS:
        raise PermissionDenied("Hanya anggota kelompoko CacingNaga yang dapat mengakses halaman ini.")
    
    theme, created = SiteTheme.objects.get_or_create(pk=1)

    if request.method == 'POST':
        form = SiteThemeForm(request.POST, instance=theme)
        if form.is_valid():
            form.save()
            return redirect('theme_settings')
    else:
        form = SiteThemeForm(instance=theme)

    presets = {
        'light': {'bg_color':'#eaf2ff', 'accent_color':'#0e5a64', 'text_color':'#1b2b5a', 'highlight_color':'#ffc107', 'surface_color':'#ffffff'},
        'dark':  {'bg_color':'#101b2d', 'accent_color':'#2b8c93', 'text_color':'#edf3ff', 'highlight_color':'#d8b15a', 'surface_color':'#18253a'},
    }

    current = {'bg_color': theme.bg_color, 'accent_color': theme.accent_color, 'text_color': theme.text_color, 'highlight_color': theme.highlight_color, 'surface_color': theme.surface_color}
    active_preset = 'Custom'
    for name, values in presets.items():
        if values == current:
            active_preset = name.title()
            break

    return render(request, 'theme/settings.html', {'form': form, 'theme': theme, 'active_preset': active_preset})
