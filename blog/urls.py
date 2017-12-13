from django.urls import path
from blog import views

urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.form_article_view, name="form_article")
]