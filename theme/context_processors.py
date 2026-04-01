from .models import SiteTheme

def site_theme(request):
    from .models import SiteTheme
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
        'user_actual_email': user_email.lower(), # Gunakan variabel baru ini di HTML
        'whitelist_emails': [e.lower() for e in whitelist]
    }