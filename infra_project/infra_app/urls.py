from django.urls import path

from . import views

app_name = 'infra_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('second/', views.second_page, name='second_page'),

]

# flake8 . - проверить что workflow на github
# actions пройдёт корректно
# isort infra_project/urls.py - если не можешь исправить
# файл вручную напиши это для неправильного файла
