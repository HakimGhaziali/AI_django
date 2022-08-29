from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .fun import funn
from .forms import CForm

def home(request):

    if request.method =='GET':

        print('hey')
        form = CForm()
        print(funn())


    elif request.method == 'POST' :

        print('how')
        print(request.POST['Form_field'])
        form= CForm(request.POST)
        #print(request.POST)
        #m = [request.POST[str(x)] for x in request.POST if x is not '']
        #print(m)
        #for i in request.POST:
            #print(str(i))
            #print(request.POST[str(i)])
        #print(request.POST[('X2')])

    return render(request ,  'index.html' , {'form': form})

    