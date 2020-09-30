from django.db import models
from .ticket import Ticket


class Comment(models.Model):
    ticket = models.ForeignKey(
        to=Ticket,
        on_delete=models.CASCADE,
        related_name='comment'
    )

    content = models.TextField(
        null=False
    )

    @classmethod
    def create(cls, ticket, content):
        return cls(ticket=ticket, content=content)

    class Meta:
        app_label = 'ticket_manager'
        verbose_name = 'comment'
        verbose_name_plural = 'comments'