from django.shortcuts import render
from . models import Experiencia
from . forms import FormularioExperiencia

# Create your views here.
# def usuariolist(request):
#     return render(request,'usuariolist.html')




def index(request):
    return render(request,'index.html')

def login_usuario(request):
    return render(request,'login_usuario.html')



def Experiencialist(request):
    get_experiencia=Experiencia.objects.all()
    data={
        'get_experiencia':get_experiencia
    }
    return render(request,'listexperiencia.html',data)

def indexFormulario(request):
    experiencia=FormularioExperiencia()
    return render(request, "formexperiencia.html",{"form":experiencia})

def procesarFormularioExperiencia(request):
    
    if 'guardar' in request.POST:        
        experiencia=FormularioExperiencia(request.POST,request.FILES)
        if experiencia.is_valid():
            experiencia.save()
            experiencia=FormularioExperiencia()
        return render(request,"formoferta.html",{"form":experiencia,"mensaje":"ok"} )

def editarExperiencia(request,id_experiencia):
    experiencia=Experiencia.objects.filter(id=id_experiencia).first()
    form=FormularioExperiencia(instance=experiencia)
    return render(request, "ExperienciaEdit.html",{"form":form,"experiencia":experiencia})

def actualizarExperiencia(request,id_experiencia):
    experiencia=Experiencia.objects.get(pk=id_experiencia)
    form=FormularioExperiencia(request.POST,instance=experiencia)
    if form.is_valid():
       form.save()
       get_experiencia=Experiencia.objects.all()
       return render(request,"listexperiencia.html",{"get_experiencia":get_experiencia})
    
def eliminarExperiencia(request, id_experiencia):
    n_experiencia=Experiencia.objects.get(pk=id_experiencia)
    n_experiencia.delete()
    experiencia=Experiencia.objects.all()
    return render(request, "listexperiencia.html",{"get_experiencia":experiencia})