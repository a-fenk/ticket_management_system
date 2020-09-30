from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from ticket_manager.forms import TicketForm
from ticket_manager.models import Ticket
from website.errors import raise_403


def add_ticket(request):
    if request.user.has_perm('ticket_manager.add_ticket'):
        if request.method == 'GET':
            form = TicketForm()

            context = {
                'form': form
            }

            return render(
                request,
                'add_ticket.html',
                context
            )

        elif request.method == 'POST':
            form = TicketForm(request.POST)
            if form.is_valid():
                Ticket.create(
                    worker=User.objects.filter(id=form.data['worker']).first(),
                    description=form.data['description'],
                    details=form.data['details']
                ).save()
                return redirect('tickets')
    else:
        return raise_403()
