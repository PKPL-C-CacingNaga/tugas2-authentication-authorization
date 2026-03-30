from django.http import HttpResponse


def show_main(request):
    return HttpResponse("Django base is running.")
