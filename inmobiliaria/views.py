from django.shortcuts import render, redirect

PROPIEDADES = [
    {'id':1,'title':'Apartamento Centro','price':'$950.000.000','rooms':3,'baths':2,'area':'90 m²','summary':'Céntrico, cerca a comercios.','images':['img/apartamento.jpg']},
    {'id':2,'title':'casa Rural','price':'$680.000.000','rooms':4,'baths':3,'area':'180 m²','summary':'Cerca al mar, excelente vista.','images':['img/casa_rural.jpg']},
    {'id':3,'title':'Apartamento Centro.','price':'$1.380.000.000','rooms':4,'baths':3,'area':'130 m²','summary':'Céntrico, cerca a comercios.','images':['img/apartamento2.jpg']},
    {'id':4,'title':'casa Rural.','price':'$1.780.000.000','rooms':4,'baths':3,'area':'180 m²','summary':'Cerca al mar, excelente vista.','images':['img/casa_rural2.jpg']},
    
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
        
        nombre = request.POST.get('nombre')
        return render(request,'inmobiliaria/confirmacion.html',{'nombre':nombre})
    return render(request,'inmobiliaria/agendar.html')
def terminos(request):
    return render(request, 'inmobiliaria/terminos.html')
