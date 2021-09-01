# from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Game
from django.urls import reverse_lazy


# Create your views here.
class GameListView(ListView):
    template_name='games/game_list.html'
    model=Game

class GameDetailView(DetailView):
    template_name='games/game_detail.html'
    model=Game

class GameCreatView(CreateView):
    template_name='games/create_list.html'
    model=Game
    fields=["name","description","purchaser"]

class GameUpdateView(UpdateView):
    template_name='games/update_list.html'
    model=Game
    fields=["name","description","purchaser"]
    
class GameDeleteView(DeleteView):
    template_name='games/delete_list.html'
    model=Game
    success_url=reverse_lazy("game_list")