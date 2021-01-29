from django.shortcuts import render,  get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from .forms import PostForm, UpdateForm, CategoryForm, AddCommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# Create your views here.

"""
def home(request):
    return render(request, "home.html", {})
"""


def LikeView(request, pk):
    post = get_object_or_404(Post, pk=pk)
    #post = post.objects.get(id=pk)
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse("article-detail", args=[str(pk)]))


class AddCommentView(CreateView):
    model = Comment
    template_name = 'add_comment.html'
    form_class = AddCommentForm

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy("home")


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ["-id"]

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(
            *args, **kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context


class AddPostView(CreateView):
    model = Post
    template_name = 'add_post.html'
    form_class = PostForm
    """fields = [
        "title", "title_tag", "body",
    ]"""


def CategoryListView(request):
    categories = Category.objects.all()
    return render(request, 'categorieslist.html', {'categories': categories})


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace("-", " "))
    return render(request, 'categories.html', {'cats': cats.replace("-", " "), 'category_posts': category_posts})


class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    form_class = CategoryForm

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AddCategoryView, self).get_context_data(
            *args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class PostUpdateView(UpdateView):
    model = Post
    template_name = "update_post.html"
    form_class = UpdateForm
    #fields = ["title", "title_tag", "body"]


class PostDeleteView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy("home")
