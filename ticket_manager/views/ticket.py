from django.shortcuts import render
from django.http import HttpResponseForbidden, HttpResponseRedirect

from ticket_manager.forms import CommentForm
from ticket_manager.models import Ticket, Comment


def ticket(request, id):
    ticket = Ticket.objects.filter(id=id).first()
    current_user = request.user

    if not (current_user.groups.filter(name='managers').exists() or current_user == ticket.worker):
        return HttpResponseForbidden()  # 403 in cases of non-manager or ticket worker login

    if request.method == 'GET':
        form = CommentForm()

        context = {
            'ticket': ticket,
            'comment': Comment.objects.filter(ticket=ticket).first(),
            'form': form
        }

        return render(
            request,
            'ticket.html',
            context
        )

    elif request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            Comment.create(
                ticket=ticket,
                content=form.data['comment']
            ).save()
            ticket.close_ticket(ticket.id)
        return HttpResponseRedirect(request.path_info)  # redirect to self
