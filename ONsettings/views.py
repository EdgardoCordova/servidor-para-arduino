from django.shortcuts import render
from django.http import JsonResponse
from .models import crc_ON
import random 
import json


# este programa lo que hace es completar una tabla inicial

def generation_view(request):
    minutos_hora = 60
    horas = 2
    num_lineas = minutos_hora * horas
    k=1
    # delete table crc_ON
    qs = crc_ON.objects.all()
    if qs:
        crc_ON.objects.all().delete()


    for i in range (1,horas+1):
    
        for j in range(0,minutos_hora):
            s1 = random.randint(0,1)
            s2 = random.randint(0,1)
            s3 = random.randint(0,1)
            s4 = random.randint(0,1)
            s5 = random.randint(0,1)
            s6 = random.randint(0,1)
            print(k,"  hora: ",i," min: ",j,"[",s1,", ",s2,", ",s3,", ",s4,", ",s5,", ",s5,"]")
            k = k + 1
            crc_ON.objects.create(circuit_id=1001, hour=i,minute=j,status1=s1,status2=s2,status3=s3,status4=s4,status5=s5,status6=s6)
    
    qs = crc_ON.objects.all()
    context = {
        'qs': qs,
    }
    return render(request, 'ONsettings/main.html', context)            

def json_generation_view(request):
    
    # abrimos queryset object de crc_ON
    qs = crc_ON.objects.all()

    # creamos una variable tipo diccionario 
    data = {}

    # dentro del diccionario va a tener una lista
    data["programa_circuitos"] = []

    # carga de lista
    for obj in qs:
        data["programa_circuitos"].append({
            "circuit_id": obj.circuit_id,
            "hour": obj.hour,
            "minute": obj.minute,
            "status1": obj.status1,
            "status2": obj.status2,
            "status3": obj.status3,
            "status4": obj.status4,
            "status5": obj.status5,
            "status6": obj.status6
        })
    with open('data.json','w') as file:     # file es un nombre alias
        json.dump(data,file,indent=4)
    
    context = {
        'qs': qs,
    }
    return render(request, 'ONsettings/json_generation.html', context)            

def json_response_view(request):
    
    # abrimos queryset object de crc_ON
    qs = crc_ON.objects.all()

    # creamos una variable tipo diccionario 
    data = {}

    # dentro del diccionario va a tener una lista
    data["programa_circuitos"] = []

    # carga de lista
    for obj in qs:
        data["programa_circuitos"].append({
            "circuit_id": obj.circuit_id,
            "hour": obj.hour,
            "minute": obj.minute,
            "status1": obj.status1,
            "status2": obj.status2,
            "status3": obj.status3,
            "status4": obj.status4,
            "status5": obj.status5,
            "status6": obj.status6
        })
    with open('data.json','w') as file:     # file es un nombre alias
        json.dump(data,file,indent=4)
    
    context = {
        'qs': qs,
    }
    return JsonResponse(data)





