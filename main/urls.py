from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('livros/', include('app02.urls')),
    path('produtos/', include('cadastroP.urls')),
    path('cadastro/', include('cadastrouser.urls')),
]
