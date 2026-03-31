from django.shortcuts import render, redirect
from .models import SiteTheme
from .forms import SiteThemeForm

def theme_settings(request):
    # Ambil tema yang ada, kalau belum ada buat baru dengan nilai default
    theme, created = SiteTheme.objects.get_or_create(pk=1)

    if request.method == 'POST':
        form = SiteThemeForm(request.POST, instance=theme)
        if form.is_valid():
            form.save()
            return redirect('theme_settings')
    else:
        form = SiteThemeForm(instance=theme)

    return render(request, 'theme/settings.html', {'form': form, 'theme': theme})