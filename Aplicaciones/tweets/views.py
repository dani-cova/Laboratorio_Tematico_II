from django.shortcuts import render
from .models import Post, Categoria
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator

def home(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True)
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset)
        ).distinct()
    return render(request,'index.html',{'posts':posts})

def detallePost(request,slug):
    post = get_object_or_404(Post,slug = slug)
    return render(request,'post.html',{'detalle_post':post})


def graficas(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact = 'graficas')
    )
    if queryset:
         posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'graficas'),
        ).distinct()

    paginator = Paginator(posts,3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request,'graficas.html',{'posts':posts})

def contador(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact = 'contador')
    )
    if queryset:
         posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'contador'),
        ).distinct() 

    paginator = Paginator(posts,3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)   
    return render(request, 'contador.html',{'posts':posts})

def registros(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact = 'registros')
    )
    if queryset:
         posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'registros'),
        ).distinct() 

    paginator = Paginator(posts,3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request,'registros.html',{'posts':posts})