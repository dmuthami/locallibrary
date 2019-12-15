from django.urls import path, include
from katalog import views

urlpatterns = [
    # path('addstreetroad/', views.AddstreetroadList.as_view()),
     path('', views.index, name='index'),
     path('books/', views.BookListView.as_view(), name='books'),
     path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
]
