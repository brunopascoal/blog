from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()
    return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'form': form})

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'post_create.html', {'form': form})

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_create.html'
    success_url = reverse_lazy('post_list')  # Redireciona para a listagem de posts após criar

    def form_valid(self, form):
        # Aqui você pode adicionar lógica extra, como definir o autor do post
        form.instance.author = self.request.user  # Definir o autor como o usuário logado
        return super().form_valid(form)