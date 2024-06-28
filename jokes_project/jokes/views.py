from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from .models import Joke
from .forms import UserRegistrationForm, JokeForm

class JokeListView(ListView):
    model = Joke
    template_name = 'jokes/list_jokes.html'

class JokeCreateView(CreateView):
    model = Joke
    form_class = JokeForm
    template_name = 'jokes/create_joke.html'
    success_url = reverse_lazy('jokes:list_jokes')

class JokeDetailView(DetailView):
    model = Joke
    template_name = 'jokes/joke_detail.html'

class JokeUpdateView(UpdateView):
    model = Joke
    form_class = JokeForm
    template_name = 'jokes/create_joke.html'
    success_url = reverse_lazy('jokes:list_jokes')

class JokeDeleteView(DeleteView):
    model = Joke
    template_name = 'jokes/joke_confirm_delete.html'
    success_url = reverse_lazy('jokes:list_jokes')

class SignupView(FormView):
    template_name = 'jokes/signup.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    