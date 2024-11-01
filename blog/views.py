from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from decouple import config
import requests
from django.core.files.base import ContentFile
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Post
from .forms import PostForm
from openai import OpenAI
from django.http import HttpResponseRedirect


def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'post_list.html', {'posts': posts})

@login_required
def add_comment(request, slug):
    post = get_object_or_404(Post, slug=slug)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user  # Define o autor como o usuário logado
            comment.post = post  # Associa o comentário ao post específico
            comment.save()
            return redirect('post_detail', slug=post.slug)
    else:
        return redirect('post_detail', slug=post.slug)
    
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.all()
    form = CommentForm()  # Apenas inicialize o formulário
    return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'form': form})

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'post_create.html', {'form': form})



api = config("API_KEY_OPENAI")
client = OpenAI(api_key=api)

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_create.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user

        # Verifica se o usuário fez upload de uma imagem
        if 'image_url' not in self.request.FILES:
            # Nenhuma imagem foi carregada, gerar imagem usando a API
            prompt = f"{self.object.title} {self.object.content[:200]}"
            
            try:
                response = client.images.generate(prompt=prompt, n=1, size="512x512")
                image_url = response.data[0].url

                # Baixar a imagem gerada pela API
                image_response = requests.get(image_url)

                if image_response.status_code == 200:
                    # Salvar a imagem no diretório de mídia definido
                    self.object.image_url.save(
                        f'{self.object.slug}.png',
                        ContentFile(image_response.content),
                        save=False
                    )
                else:
                    print("Erro ao baixar a imagem")

            except Exception as e:
                print(f"Erro ao gerar imagem: {e}")
        else:
            # Imagem foi carregada pelo usuário, não é necessário gerar
            pass

        # Salva o objeto no banco de dados
        self.object.save()
        # Salva os campos ManyToMany
        form.save_m2m()
        # Redireciona para a URL de sucesso
        return HttpResponseRedirect(self.get_success_url())
