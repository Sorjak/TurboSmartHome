# views go in here
from __future__ import absolute_import, unicode_literals

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from lib.flux_led import *

# @login_required(login_url='/accounts/login/')
def toggle_lights(request):
    addrs = BulbSeeker().discover(2)
    if not addrs:
        return JsonResponse({'result' : False, 'data' : "Could not find any lights."})

    results = {}

    for a in addrs:
        try:
            bulb = WifiLedBulb(a)
        except Exception as e:
            print("Error getting bulb at {}".format(a))
            return JsonResponse({'result' : False, 'data' : "{}".format(e)})

        bulb.refreshState()

        print(bulb.is_on)

        if bulb.is_on:
            bulb.turnOff()
            results[a] = "Turned Off"
        else:
            bulb.turnOn()
            results[a] = "Turned On"

    return JsonResponse({'result' : True, 'data' : results})



        
