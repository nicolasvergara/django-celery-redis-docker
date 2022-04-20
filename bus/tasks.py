from celery import shared_task

from django.apps import apps
from django.utils import timezone

@shared_task
def change_status_of_unvalid_tickets():
    _ticket_model = apps.get_model('bus', 'Ticket')#hack to avoid circular import
    tickets = _ticket_model.objects.filter(status='AVATIBLE')
    if tickets:
        now = timezone.now()
        for obj in tickets:
            if obj.departure_time <= now:
                obj.status = 'EXPIRED'
                obj.save() 