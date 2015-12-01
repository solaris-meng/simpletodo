from django.shortcuts import render

from django.template import RequestContext, loader
from django.http import HttpResponse
from django.shortcuts import redirect

# Create your views here.
def index_view(request):
    ctx = {}
    if not request.user.is_authenticated():
        ctx['result'] = 'not authenticated'
        context = RequestContext(request, ctx)
        template = loader.get_template('home/index.html')
        return HttpResponse(template.render(context))
    return redirect('/todo')
