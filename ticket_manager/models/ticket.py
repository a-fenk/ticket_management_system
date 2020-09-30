from enum import Enum

from django.db import models
from django.contrib.auth.models import User
from django_enum_choices.fields import EnumChoiceField


class TicketStatus(Enum):
    OPEN = 'open'
    CLOSED = 'closed'


class Ticket(models.Model):
    worker = models.ForeignKey(
        to=User,
        limit_choices_to={'groups__name': "workers"},
        on_delete=models.CASCADE,
    )

    status = EnumChoiceField(
        enum_class=TicketStatus,
        default=TicketStatus.OPEN
    )

    description = models.CharField(
        max_length=511,
        null=False,
    )

    details = models.TextField(
        null=False
    )

    @classmethod
    def close_ticket(cls, id):
        return cls.objects.filter(id=id).update(status=TicketStatus.CLOSED)

    @classmethod
    def create(cls, worker, description, details):
        return cls(worker=worker, description=description, details=details)

    def update(self, worker, description, details):
        self.worker = worker
        self.description = description
        self.details = details
        return self.save()

    def __str__(self):
        return self.description[:100] + '...'

    class Meta:
        app_label = 'ticket_manager'
        verbose_name = 'ticket'
        verbose_name_plural = 'tickets'
