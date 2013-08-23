from django.http import HttpResponse


def home_page(request):
    return HttpResponse(u'<html><title>To-Do lists</title></html>')
