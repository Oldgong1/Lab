from django.shortcuts import render
import datetime 

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(request, "independenceday/index.html", {
        "independenceday": now.month == 3 and now.day == 6
    })
