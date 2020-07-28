from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.generic.edit import FormView
from django.contrib import messages
import socket

from .forms import DateForm


class vistaConf(FormView):
    def getUrl():
        return '/configure/'
    def get(self, request, *arg, **kargs):
        form = DateForm(request.GET or None)
        context={
            'form': form
        }
        return render(request,'index/conf.html',context)
    
    def post(self, request, *arg, **kargs):
        form = DateForm(request.POST or None)

        print(form)
        print('form',form.data['date'])
        #form =form.data['date']
        

        if form.is_valid():
            self.object = form.save(commit=False)
            self.object.save()
        
        return redirect('/configure/')
    


class vistaClass(View):

    #template = 'index.html'

    def get(self, request, *arg, **kargs):
        return render(request,'index/index.html')
    
   
    def post(self, request, *arg, **kargs):
        #boton de despachar
        if 'btn1' in request.POST.keys():

            try:
                print("boton despachar")
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect( ('raspy2412.ddns.net',7080) )
                print("Ya conecto ;v")
                mensaje = "SERVO"
                s.send(bytes(mensaje, "utf-8"))
                msg = s.recv(1024)
                #print("El peso actual de del dispensador es de: ",msg.decode("utf-8"),"g")
                peso= msg.decode("utf-8") # Obtener solo la cantidad el numero lo regresa como String
                s.close()
                print()
                print("ADIOS")
                messages.info(request, peso)

                return render(request,'index/index.html')
            except:
                    messages.info(request, 'Error')
                    print("No se pudo establecer conexion ;v")
                    return render(request,'index/index.html')
        #boton peso
        if 'btn2' in request.POST.keys():
            try:
                print("boton peso")
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect( ('raspy2412.ddns.net',7080) )
                mensaje = "PESO"
                s.send(bytes(mensaje, "utf-8"))
                msg = s.recv(1024)
                #print("El peso actual del dispensador es de: ",msg.decode("utf-8"),"g")
                peso= msg.decode("utf-8") # Obtener solo la cantidad el numero lo regresa como String
                s.close()
                print()
                print("ADIOS")
                messages.info(request, peso)

                return render(request,'index/index.html')

            except:
                messages.info(request, 'Error')
                print("No se pudo establecer conexion ;v")
                return render(request,'index/index.html')

        #Boton para acceder a vista de poner horario
        if 'btn3' in request.POST.keys():
            r = vistaConf.getUrl()
            return redirect(r)