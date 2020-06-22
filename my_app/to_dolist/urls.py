
from django.urls import path
from . import views


urlpatterns = [
   path('', views.home, name='home'),
   path('delete/<key>', views.delete, name="delete"),
   path('edit/<key>', views.edit, name="edit"),

]
