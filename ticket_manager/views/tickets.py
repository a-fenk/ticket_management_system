from django.shortcuts import render
from django.http import HttpResponseForbidden

from ticket_manager.models import Ticket


def tickets(request):
    if request.method == 'GET':

        current_user = request.user
        if current_user.groups.filter(name='managers').exists():
            tickets = Ticket.objects.all()
        elif current_user.groups.filter(name='workers').exists():
            tickets = Ticket.objects.filter(worker=current_user)
        else:
            return HttpResponseForbidden()

        context = {
            'tickets': tickets,
        }

        return render(
            request,
            'tickets.html',
            context
        )
