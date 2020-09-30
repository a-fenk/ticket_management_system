import logging

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management import BaseCommand

from ticket_manager.models import Ticket, Comment


class Command(BaseCommand):
    def handle(self, *args, **options):
        ticket_content_type = ContentType.objects.get_for_model(Ticket)
        comment_content_type = ContentType.objects.get_for_model(Comment)

        workers, created = Group.objects.get_or_create(name='workers')
        managers, created = Group.objects.get_or_create(name='managers')

        try:
            add_comment_permission = Permission.objects.get(
                content_type=comment_content_type,
                codename='add_comment'
            )
            view_ticket_permission = Permission.objects.get(
                content_type=ticket_content_type,
                codename='view_ticket'
            )
            add_ticket_permission = Permission.objects.get(
                content_type=ticket_content_type,
                codename='add_ticket'
            )
            edit_ticket_permission = Permission.objects.get(
                content_type=ticket_content_type,
                codename='change_ticket'
            )
        except Permission.DoesNotExist:
            logging.warning('Can\'t find permission. Please check if you have applied all migrations')
        else:

            # workers permissions
            workers.permissions.add(add_comment_permission)
            workers.permissions.add(view_ticket_permission)

            # managers permissions
            managers.permissions.add(view_ticket_permission)
            managers.permissions.add(add_ticket_permission)
            managers.permissions.add(edit_ticket_permission)

            print('Permissions successfully added')

