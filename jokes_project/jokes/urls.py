from django.urls import path
from .views import (
    JokeListView, JokeCreateView, JokeDetailView, JokeUpdateView,
    JokeDeleteView, SignupView
)

app_name = 'jokes'

urlpatterns = [
    path('', JokeListView.as_view(), name='list_jokes'),
    path('new/', JokeCreateView.as_view(), name='create_joke'),
    path('<int:pk>/', JokeDetailView.as_view(), name='joke_detail'),
    path('<int:pk>/edit/', JokeUpdateView.as_view(), name='update_joke'),
    path('<int:pk>/delete/', JokeDeleteView.as_view(), name='delete_joke'),
    path('signup/', SignupView.as_view(), name='signup'),
]

# jokes_project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jokes/', include('jokes.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
