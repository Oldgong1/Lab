from django.shortcuts import render

import datetime

# Create your views here.

def index(request):
    now = datetime.datetime.now()
    return render(request, "republic_day/index.html", {"republic_day": now.day ==1 and now.month ==7
    })

