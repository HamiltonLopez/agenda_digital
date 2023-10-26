from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='inicio'),
    path('list/',views.list,name='lista'),
    path('add/',views.addContact,name='agregar'),
    path('edit/<int:id>',views.editContact,name='editar'),
    path('delete/<int:id>/',views.deleteContact,name='eliminar'),
]