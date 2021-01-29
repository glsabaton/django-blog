from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView, PostUpdateView, PostDeleteView, AddCategoryView, CategoryView, CategoryListView, LikeView, AddCommentView
from .models import Post
urlpatterns = [
    #path("", views.HomeView, name="home")
    path("", HomeView.as_view(), name="home"),
    path("articte/<int:pk>", ArticleDetailView.as_view(), name="article-detail"),
    path("add_post/", AddPostView.as_view(), name='add_post'),
    path("article/edit/<int:pk>", PostUpdateView.as_view(), name='update_post'),
    path("article/<int:pk>/remove", PostDeleteView.as_view(), name='delete_post'),
    path("add_category/", AddCategoryView.as_view(), name='add_category'),
    path("category/<str:cats>/", CategoryView, name="category"),
    path("categories/", CategoryListView, name="categories"),
    path("like/<int:pk>/", LikeView, name="like_post"),
    path("add_comment/<int:pk>", AddCommentView.as_view(), name="add_comment")
]
