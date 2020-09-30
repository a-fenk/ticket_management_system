from django.forms import ModelForm

from ticket_manager.models import Ticket


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['worker', 'description', 'details']
