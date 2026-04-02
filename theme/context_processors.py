from .models import SiteTheme


def _hex_to_rgb(value):
    value = value.lstrip('#')
    if len(value) != 6:
        return 255, 255, 255
    return tuple(int(value[i:i + 2], 16) for i in (0, 2, 4))


def _is_dark_color(value):
    red, green, blue = _hex_to_rgb(value)
    luminance = (0.2126 * red + 0.7152 * green + 0.0722 * blue) / 255
    return luminance < 0.5


def site_theme(request):
    theme, _ = SiteTheme.objects.get_or_create(pk=1)
    
    user_email = ""
    if request.user.is_authenticated:
        user_email = request.user.email
        
        if not user_email and hasattr(request.user, 'socialaccount_set'):
            social_acc = request.user.socialaccount_set.first()
            if social_acc:
                user_email = social_acc.extra_data.get('email', '')

    whitelist = [
        'a.anggara.bayuadji.p@gmail.com', 
        'aaronsuhaendi@gmail.com', 
        'rizkyantariksa02@gmail.com', 
        'samuelindriano@gmail.com', 
        'wildanhidayatirl@gmail.com',
    ]
    
    return {
        'theme': theme,
        'theme_mode': 'dark' if _is_dark_color(theme.bg_color) else 'light',
        'user_actual_email': user_email.lower(),
        'whitelist_emails': [e.lower() for e in whitelist],
    }
