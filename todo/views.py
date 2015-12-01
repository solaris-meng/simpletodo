from django.shortcuts import render

from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Todo,TodoFile
from uuid import uuid4
import datetime
import traceback
import json
import os

# Create your views here.
def todo_user_view(request):
    ctx = {}
    if not request.user.is_authenticated():
        ctx['result'] = 'not authenticated'
        context = RequestContext(request, ctx)
        template = loader.get_template('index/user_invalid.html')
        return HttpResponse(template.render(context))

    user = request.user
    todos = Todo.objects.filter(user=user)
    ctx['todo'] = todos
    ctx['result'] = 'success'

    context = RequestContext(request, ctx)
    template = loader.get_template('todo/todo_user.html')
    return HttpResponse(template.render(context))

def todo_import_view(request):
    ctx = {}
    if not request.user.is_authenticated():
        ctx['result'] = 'not authenticated'
        context = RequestContext(request, ctx)
        template = loader.get_template('index/user_invalid.html')
        return HttpResponse(template.render(context))

    user = request.user
    ctx['result'] = 'success'

    context = RequestContext(request, ctx)
    template = loader.get_template('todo/todo_import.html')
    return HttpResponse(template.render(context))

def todo_update_handler(request, tid, opt):
    print 'debug',request.user,tid,opt
    rv = {}
    try:
        if opt == 'done':
            status = 'done'
        else:
            status = 'abort'
        todo = Todo.objects.get(id=tid)
        todo.status = status
        todo.save()

        rv['result'] = 'success'
        rv['status'] = status
        r = json.dumps(rv)
        return HttpResponse(r, content_type="application/json")
    except Exception, e:
        err= traceback.format_exc()
        rv['result'] = 'failed, %s' % err
        r = json.dumps(rv)
        return HttpResponse(r, content_type="application/json")

    r = json.dumps(rv)
    return HttpResponse(r, content_type="application/json")


def todo_add_handler(request):
    if request.method == 'POST':
        rv = {}
        try:
            print request.POST

            content = request.POST['todo-content']
            start = request.POST['datepicker-start']
            end = request.POST['datepicker-end']

            todo_check = Todo.objects.filter(content=content)
            if todo_check:
                rv['result'] = 'failed repeat submit'
                r = json.dumps(rv)
                return HttpResponse(r, content_type="application/json")

            time_start = datetime.datetime.strptime(start, '%m/%d/%Y')
            time_end = datetime.datetime.strptime(end, '%m/%d/%Y')
            status = 'to do'
            todo = Todo(user=request.user,
                        upload_id='notset',
                        time_start=time_start,
                        time_end=time_end,
                        status=status,
                        content=content)
            todo.save()
            rv['result'] = 'success'
        except Exception, e:
            import traceback
            err= traceback.format_exc()
            print err
            rv['result'] = 'failed %s' % err
        r = json.dumps(rv)
        return HttpResponse(r, content_type="application/json")
    return HttpResponse('invalid')

def todo_import_handler(request):
    if request.method == 'POST':
        try:
            print request.POST
            print request.FILES
            
            # Parse data
            data = request.FILES['uploadfile'].read()
            #print 'Data:',data
            lines = data.split('\n')
            for l in lines:
                if l == '':
                    continue
                tokens = l.split('/')
                #print tokens

                dates = tokens[0].split('-')
                start,end = dates[0],dates[1]
                time_start = datetime.datetime.strptime(start, '%Y.%m.%d')
                if end == '' :
                    time_end = time_start
                else:
                    time_end = datetime.datetime.strptime(end, '%Y.%m.%d')
                status = tokens[1]
                content = tokens[2]
                print 'line:',start,end,status,content

                todo_check = Todo.objects.filter(content=content)
                if todo_check:
                    continue

                todo = Todo(user=request.user,
                            upload_id='notset',
                            time_start=time_start,
                            time_end=time_end,
                            status=status,
                            content=content)
                todo.save()
            
            todo_file = TodoFile(uploadfile = request.FILES['uploadfile'],
                            user=request.user,
                            upload_id=uuid4().hex)
            todo_file.save()
            return HttpResponse('succss')
        except Exception, e:
            import traceback
            err= traceback.format_exc()
            print err
            return HttpResponse('failed, %s' % err)
        return HttpResponse('succss')
    return HttpResponse('failed')
