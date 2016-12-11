from django.http import HttpResponse

def index(request):
    return HttpResponse("YO."
                        "<h1>This is the music homepage</h1>"
                        "<p>You like?</p>")
