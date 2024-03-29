from django.urls import path
# Импортируем созданное нами представление
from .views import NewsList, NewsDetail, NewsSearch, NewsCreate, NewsUpdate, NewsDelete


urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем новостям у нас останется пустым,
   # чуть позже станет ясно почему.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   path('', NewsList.as_view(), name='news_list'),
   path('<int:pk>', NewsDetail.as_view(), name='news_detail'),
   path('search/', NewsSearch.as_view(), name='news_search'),
   path('create/', NewsCreate.as_view(), name='news_create'),
   path('articles/create/', NewsCreate.as_view(), name='article_create'),
   path('<int:pk>/edit/', NewsUpdate.as_view(), name='news_update'),
   path('articles/<int:pk>/edit/', NewsUpdate.as_view(), name='news_update'),
   path('<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
   path('articles/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
]