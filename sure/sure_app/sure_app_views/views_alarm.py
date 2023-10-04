from django.shortcuts import render
from django.http import JsonResponse

from ..models import Alarm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def read_alarm(request, alarm_id):
    alarm = Alarm.objects.get(id=alarm_id)
    alarm.is_read = True 
    alarm.save()
    print('read_alarm')

    return JsonResponse({'msg': '알람 읽기 성공'}, status=200)