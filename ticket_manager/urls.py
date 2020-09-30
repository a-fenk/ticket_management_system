from django.urls import path

from ticket_manager import views

urlpatterns = [
    path('', views.base, name='home'),
    path('tickets/', views.tickets, name='tickets'),
    path('tickets/add', views.add_ticket, name='add_ticket'),
    path('tickets/id=<id>', views.ticket, name='ticket'),
    path('tickets/id=<id>/edit', views.edit_ticket, name='edit_ticket'),
]