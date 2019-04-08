from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.forms import UserCreationForm

@require_http_methods(['GET', 'POST'])
def vocab(request):
    if request.method == 'GET':
        params = request.GET
        return HttpResponse('you got it')
    else:
        params = request.POST
        return HttpResponse('you posted it')
