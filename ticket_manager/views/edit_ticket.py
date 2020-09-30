from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect

from ticket_manager.forms import TicketForm
from ticket_manager.models import Ticket


def edit_ticket(request, id):
    ticket = Ticket.objects.filter(id=id).first()
    if request.user.has_perm('ticket_manager.change_ticket'):
        if request.method == 'GET':
            form = TicketForm(initial={
                'worker': ticket.worker,
                'description': ticket.description,
                'details': ticket.details
            })

            context = {
                'form': form
            }

            return render(
                request,
                'edit_ticket.html',
                context
            )

        elif request.method == 'POST':
            form = TicketForm(request.POST)
            if form.is_valid():
                ticket.update(
                    worker=User.objects.filter(id=form.data['worker']).first(),
                    description=form.data['description'],
                    details=form.data['details']
                )
                return redirect('ticket', id)
            print(form)
    else:
        return HttpResponseForbidden()
