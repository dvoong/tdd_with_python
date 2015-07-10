from django.http import HttpResponse

def home_page(request):
    import logging
    logging.info('home_page')
    return HttpResponse('home_page')
