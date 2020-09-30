from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),  # /login, /logout, /signup
    path('', include('ticket_manager.urls')),  # /, /tickets, /tickets/id=<id>, /tickets/add, /tickets/id=<id>/edit
]
