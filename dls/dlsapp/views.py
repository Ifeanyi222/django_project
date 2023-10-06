from django.http import HttpResponse
from django.template import loader
from .models import Dls


# Create your views here.
def dlsapp(request):
    mydlsapp = Dls.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mydlsapp': mydlsapp,
    }
    return HttpResponse(template.render(context, request))



def  details(request, id):
    mydlsapp = Dls.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mydlsapp': mydlsapp
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())
