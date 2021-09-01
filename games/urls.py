
from django.urls import path
from .views import GameListView,GameDetailView,GameUpdateView,GameCreatView,GameDeleteView

urlpatterns=[
    path("",GameListView.as_view(),name="game_list"),
    path("<int:pk>/",GameDetailView.as_view(),name="game_detail"),
    path("<int:pk>/update/",GameUpdateView.as_view(),name="update_list"),
    path("create/",GameCreatView.as_view(),name="create_list"),
    path("<int:pk>/delete/",GameDeleteView.as_view(),name="delete_list"),

]