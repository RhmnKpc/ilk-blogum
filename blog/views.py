from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.utils import timezone
from .models import Post
from django.http import HttpResponse
from django.shortcuts import redirect
from blog.models import Post
from blog.models import Contact
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect


def post_list(request):
    posts = Post.objects.filter(yayin_tarihi__lte=timezone.now()).order_by('-yayin_tarihi')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.yazar = request.user
            post.yayin_tarihi = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.yazar = request.user
            post.yayin_tarihi = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def about(request):
    """ Hakkımda Sayfası """
    # last_db = Post.objects.filter(is_active=True).order_by('-time')[:3]
    return render(request, 'blog/about.html', {

    })


def iletisim(request):
    if (request.method == 'POST'):
        isim = request.POST['isim']
        mail = request.POST['mail']
        telefon = request.POST['phone']
        mesaj = request.POST['message']
        contact_obj = Contact(isim=isim, mail=mail, telefon=telefon, mesaj=mesaj)
        contact_obj.save()
        return render(request, 'blog/iletisim.html', {'contact_obj': contact_obj, 'is_registered': True})

    else:
        return render(request, 'blog/iletisim.html', {

})
