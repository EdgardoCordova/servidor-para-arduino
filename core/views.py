# esta sera el view principal, que llama el main.html
from django.shortcuts import render
from ONsettings.models import crc_ON

# Create your views here.

def home_view(request):
    qs = crc_ON.objects.all()
    context = {
        'qs': qs,
    }
    return render(request, 'main.html', context)
