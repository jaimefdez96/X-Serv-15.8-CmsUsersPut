from django.shortcuts import render 
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Contents

FORMULARIO = """
<form action="" method="POST">
    Puede modificar el contenido aquí: <br>
    Contenido: <input type="text" name="content"<br>
    <input type = "submit" value = "Enviar"> 
</form>
"""
# Create your views here.
def barra(request):
    if request.user.is_authenticated():
        logged = 'Logged in as ' + request.user.username 
        logged += '. <a href=/logout>Logout</a>'
    else:
        logged = 'Not logged in.' + '<a href=/login>Login</a>'

    if request.method == 'GET':
        all_contents = Contents.objects.all()
        response = '<h1>Contenidos random</h1><br>'
        response += '<h2>Pinche en uno de los nombres para ver los contenidos</h2>'
        response += '<ul>'
        for one_content in all_contents:
            response += '<li>' + '<a href = /' + str(one_content.id) + ">" + one_content.name + "</a>"
        response += '</ul><br>'     
        return HttpResponse(response + logged)
    else:
        return HttpResponse('<h1>405 Method Error</h1>')

@csrf_exempt
def content(request, num):
        if request.method == 'POST':
            try:
                this_content = Contents.objects.get(id = int(num))
                this_content.content = request.POST['content']
                this_content.save()
            except Contents.DoesNotExist:
                return HttpResponse('<h2>404 Not Found</h2>')
            link = '<h2>El contenido ha sido modificado con éxito</h2><br>'
            link += '<a href = />Volver a la página principal</a><br>'
            return HttpResponse(link)
        elif request.method == 'GET':
            try:
                request_content = Contents.objects.get(id =  int(num))
            except Contents.DoesNotExist:
                return HttpResponse('<h2>404 Not Found</h2>')
            response = 'Titulo: ' + request_content.name +'<br>'
            response += 'Contenido: ' + request_content.content + '<br>'
            response += "<a href=/> Volver a la página principal </a><br>"
            if request.user.is_authenticated():
                response += FORMULARIO
            return HttpResponse(response)
        else:
            return HttpResponse('<h1>405 Method Error</h1>')

