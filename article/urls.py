from django.urls import path
from .views import (
    ArticleListView,
    ArticleUpdateView,
    ArticleConfirmDeleteView,
    ArticleDetailView,
    ArticleCreateView,
)
urlpatterns = [
    path('yangi_post/', ArticleCreateView.as_view(), name='yangi_post'),
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('<int:pk>/delete/', ArticleConfirmDeleteView.as_view(), name='article_confirm_delete'),
    path('', ArticleListView.as_view(), name='article_list'),
]