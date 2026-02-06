from django.urls import path
from .views import HomePageView, CreateView
urlpatterns =[
    path('home/', HomePageView.as_view(), name='home'),
    path('article/', CreateView.as_view(), name='article'),

]