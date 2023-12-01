from django.shortcuts import render
from . models import Oferta
from . forms import FormularioOferta

# Create your views here.
# def usuariolist(request):
#     return render(request,'usuariolist.html')




def index_empresa(request):
    return render(request,'index_empresa.html')


def Ofertalist(request):
    get_oferta=Oferta.objects.all()
    data={
        'get_oferta':get_oferta
    }
    return render(request,'login_empresa.html',data)

def indexFormulario(request):
    oferta=FormularioOferta()
    return render(request, "formusuario.html",{"form":oferta})

def procesarFormulario(request):
    
    if 'guardar' in request.POST:        
        oferta=FormularioOferta(request.POST,request.FILES)
        if oferta.is_valid():
            oferta.save()
            oferta=FormularioOferta()
        return render(request,"formusuario.html",{"form":oferta,"mensaje":"ok"} )

def editarUsuario(request,id_oferta):
    oferta=Oferta.objects.filter(id=id_oferta).first()
    form=FormularioOferta(instance=oferta)
    return render(request, "UsuarioEdit.html",{"form":form,"oferta":oferta})

def actualizarUsuario(request,id_oferta):
    oferta=Oferta.objects.get(pk=id_oferta)
    form=FormularioOferta(request.POST,instance=oferta)
    if form.is_valid():
       form.save()
       get_oferta=Oferta.objects.all()
       return render(request,"login_empresa.html",{"get_oferta":get_oferta})
    
def eliminarUsuario(request, id_oferta):
    n_oferta=Oferta.objects.get(pk=id_oferta)
    n_oferta.delete()
    oferta=Oferta.objects.all()
    return render(request, "login_empresa.html",{"get_oferta":oferta})