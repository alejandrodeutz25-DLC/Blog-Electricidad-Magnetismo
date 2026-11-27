from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm


def inicio(request):
    return render(request, "posts/inicio.html")


def lista_posts(request):
    posts = Post.objects.filter(estado="publicado").order_by("-fecha_creacion")
    return render(request, "posts/lista_posts.html", {"posts": posts})


def detalle_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "posts/detalle_post.html", {"post": post})


def crear_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect("detalle_post", pk=post.pk)
    else:
        form = PostForm()
    return render(request, "posts/form_post.html", {"form": form, "titulo_pagina": "Nuevo post"})


def editar_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect("detalle_post", pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, "posts/form_post.html", {"form": form, "titulo_pagina": "Editar post"})


def eliminar_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect("lista_posts")
    return render(request, "posts/eliminar_post.html", {"post": post})