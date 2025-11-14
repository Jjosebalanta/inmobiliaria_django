from django.shortcuts import render, redirect
# Sample in-memory properties
PROPIEDADES = [
    {'id':1,'title':'Apartamento Centro','price':'$250.000.000','rooms':3,'baths':2,'area':'90 m²','summary':'Céntrico, cerca a comercios.','images':['img/apartamento.jpg']},
    {'id':2,'title':'casa Rural','price':'$480.000.000','rooms':4,'baths':3,'area':'180 m²','summary':'Cerca al mar, excelente vista.','images':['img/casa_rural.jpg']},
]

def home(request):
    latest = PROPIEDADES
    return render(request,'inmobiliaria/index.html',{'propiedades':latest})
 
def detalle(request, pid):
    prop = next((p for p in PROPIEDADES if p['id']==int(pid)), None)
    if not prop:
        return redirect('home')
    return render(request,'inmobiliaria/detalle.html',{'prop':prop})

def agendar(request):
    if request.method=='POST':
        # No backend persistence; simulate confirmation
        nombre = request.POST.get('nombre')
        return render(request,'inmobiliaria/confirmacion.html',{'nombre':nombre})
    return render(request,'inmobiliaria/agendar.html')
