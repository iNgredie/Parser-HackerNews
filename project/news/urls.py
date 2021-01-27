from django.urls import path

from .views import NewsListView

urlpatterns = [
    path('posts/', NewsListView.as_view()),
]
