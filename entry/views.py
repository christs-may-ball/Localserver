import datetime

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Ticket

def index(request):
    timestamp = timezone.now().timestamp();
    tickets = [(t.status, t.last_name, t.first_name, (t.time is None), t.pk) for t in Ticket.objects.all()]
    tickets.sort()
    return render(request, 'index.html', {'tickets': tickets, 'timestamp': timestamp})

def return_ticket(ticket):
	if ticket.time and (timezone.now() - ticket.time).seconds > 4:
		status = 'C'
	else:
		status = ticket.status
		ticket.time = timezone.now()
		ticket.save()
	return JsonResponse(dict(
    	status=status,
    	first_name=ticket.first_name,
    	last_name=ticket.last_name,
    ))

def crsid(request, crsid):
    ticket = get_object_or_404(Ticket, crsid=crsid)
    return return_ticket(ticket)

def pk(request, pk):
    ticket = get_object_or_404(Ticket, pk=int(pk[:-1]))
    return return_ticket(ticket)

def time(request, timestamp):
    next_timestamp = timezone.now().timestamp();
    news = [t.pk for t in Ticket.objects.filter(time__gte=datetime.datetime.fromtimestamp(float(timestamp), timezone.get_default_timezone()))]
    return JsonResponse(dict(
        timestamp=next_timestamp,
        news=news,
    ))