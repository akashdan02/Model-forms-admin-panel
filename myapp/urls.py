from django.contrib import admin
from django.urls import path
from .views import application, show, edit, delete, update
urlpatterns = [
    path('admin/', admin.site.urls),
    path('application', application),
    path('show', show),
    path('edit/<int:id>', edit),
    path('update/<int:id>', update),
    path('delete/<int:id>', delete),

]
