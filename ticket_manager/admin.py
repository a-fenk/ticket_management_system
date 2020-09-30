from django.contrib import admin

from .models import Ticket

@admin.register(Ticket)
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('status',)

    class Meta:
        model = Ticket