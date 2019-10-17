from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datacenter.models import get_duration
from datacenter.models import format_duration
from datacenter.models import is_visit_long


def storage_information_view(request):
    visits = Visit.objects.all()
    remains = visits.filter(leaved_at=None)
    non_closed_visits = []
    for visit in remains:
        passcard = visit.passcard
        duration = get_duration(visit)
        non_closed_visits.append(
            {
                "who_entered": passcard.owner_name,
                "entered_at": visit.entered_at,
                "duration": format_duration(duration),
                'is_strange': is_visit_long(visit)
            }
        )
    context = {
        "non_closed_visits": non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
