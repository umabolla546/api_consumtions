from django.shortcuts import render
import requests
import json

# Create your views here.


def get_client_ip(request):
    ip = request.META.get('HTTP_X_FORWARDED_FOR','') or request.META.get('REMOTE_ADDR')
    print(ip)
    #url="http://api.ipstack.com/192.168.43.11?access_key=58a6e62ba64301bc068726d65c8c38b6"
    url="http://api.ipstack.com/"+str(ip)+"?access_key=58a6e62ba64301bc068726d65c8c38b6"
    response=requests.get(url)
    data=response.json()
    return render(request,'ip.html',data)