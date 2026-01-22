from django.http import HttpResponse

def home(request):
  return HttpResponse('<h2>Homepage</h2>')