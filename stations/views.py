from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .models import Station, Parameter, User
from .serializers import StationSerializer, ParameterSerializer
import geocoder
import json

def login(request):
    if request.method == 'GET':
        return render(request, 'stations/index.html')
    else:
        username = request.POST.get('username')
        if (User.objects.all().filter(name=username).exists()):
            if (User.objects.all().filter(name=username).first().password==request.POST.get('password')):
                return redirect('menu')
            else:
                return render(request, 'stations/index.html')
        else:
            return render(request, 'stations/index.html')    

def signin(request):
    if request.method == 'GET':
        return render(request, 'stations/index5.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if (User.objects.all().filter(name=username).exists()==False):
            if (User.objects.all().filter(email=email).exists()==False):
                station = User(name=username,email=email,password=password,favorites="")
                station.save()
                return redirect('index')
            else:
                return render(request, 'stations/index5.html')    
        else:
            return render(request, 'stations/index5.html')        

def menu(request):
    if request.method == 'POST':
        statname = request.POST.get('station-name')
        if (Station.objects.all().filter(name=statname).exists()==False)and(statname!=""):
            g = geocoder.ip('me')
            geolocat = str(g.latlng[0])+","+str(g.latlng[1])
            station = Station(name=statname,location=geolocat)
            station.save()
        return redirect('menu')
    else:
        all_stations = Station.objects.all()
        all_params = Parameter.objects.all()
        return render(request, 'stations/index4.html', {'stations': all_stations, 'parameters':all_params})

def create_parameter(request,station):
    if request.method == 'POST':
        paramname = request.POST.get('parameter-name')
        if (paramname!=""):
            check_station = Station.objects.all().filter(name=station).first()
            parameter = Parameter(name=paramname,station=check_station,readings="")
            parameter.save()
        return redirect('menu')    

def check_data(request,station,name,type_chart='line'):
    if request.method == 'GET':
        check_station = Station.objects.all().filter(name=station).first()
        check_parameter = Parameter.objects.all().filter(name=name,station=check_station).first()
        values = check_parameter.readings
        dates = check_parameter.dates
        if (values != ""):
            values_list = [float(item) for item in values.split(",")]
        else:
            values_list = [""]    
        if (dates != ""):
            dates_list = dates.split(",")
        else:
            dates_list = [""]  
        return render(request, 'stations/index2.html', {'station': check_station, 'parameter':check_parameter, 'values':values_list, 'dates':dates_list, 'type':type_chart})
    else:
        return redirect('menu')

def check_location(request,station,name):
    check_station = Station.objects.all().filter(name=station).first()
    check_parameter = Parameter.objects.all().filter(name=name,station=check_station).first()
    coordinates = check_parameter.location
    #coordinates = check_station.location
    f = open('stations/k.json', "r")
    api_key = json.loads(f.read())["key"]
    return render(request, 'stations/index3.html', {'station': check_station, 'parameter': check_parameter,'coordinates':coordinates, 'key':api_key})

def delete_station(request,station_id):
    del_entry = Station.objects.all().filter(id=station_id).first()
    del_entry.delete()
    return redirect('menu')

def delete_parameter(request,parameter_id):
    del_entry = Parameter.objects.all().filter(id=parameter_id).first()
    del_entry.delete()
    return redirect('menu') 

@api_view(['GET', 'POST'])
def api_station(request, station_id=0):
    if station_id==0:
        try:
            stations = Station.objects.all()
        except Station.DoesNotExist:
            raise Http404()
        serialized_station = StationSerializer(stations, many=True)    
    else:
        try: 
            station = Station.objects.get(id=station_id)
        except Station.DoesNotExist:
            raise Http404()    
        serialized_station = StationSerializer(station)     
    if request.method == 'POST':
        new_station_data = request.data
        new_station = Station(name=new_station_data['name'],date=new_station_data['date'])
        new_station.save()
        stations = Station.objects.all()    
        serialized_station = StationSerializer(stations, many=True)
    return Response(serialized_station.data)

@api_view(['GET', 'POST'])
def api_parameter(request, parameter_id=0):
    if parameter_id==0:
        try:
            parameters = Parameter.objects.all()
        except Parameter.DoesNotExist:
            raise Http404()
        serialized_parameter = ParameterSerializer(parameters, many=True) 
    else:    
        try:
            parameter = Parameter.objects.get(id=parameter_id)
        except Parameter.DoesNotExist:
            raise Http404()
        serialized_parameter = ParameterSerializer(parameter)
    if request.method == 'POST':
        new_parameter_data = request.data
        if (type(new_parameter_data['station']) == int):
            default_station = Station.objects.all().filter(id=new_parameter_data['station']).first()
        else:
            default_station = Station.objects.all().filter(id=1).first()
        new_parameter = Parameter(station=default_station,name=new_parameter_data['name'],readings="",dates="")
        new_parameter.save()
        parameters = Parameter.objects.all()    
        serialized_parameter = ParameterSerializer(parameters, many=True)    
    return Response(serialized_parameter.data)

@api_view(['GET', 'POST'])
def api_values(request, parameter_id):
    if request.method == 'POST':
        if (type(parameter_id)==int):
            new_data = request.data
            default_parameter = Parameter.objects.all().filter(id=parameter_id).first()
            if default_parameter.readings != "":
                default_parameter.readings = default_parameter.readings+","+new_data['readings']
            else:
                default_parameter.readings = new_data['readings']
            if default_parameter.dates != "":         
                default_parameter.dates = default_parameter.dates+","+new_data['dates']
            else:    
                default_parameter.dates = new_data['dates']
            default_parameter.location = new_data['location'] 
            default_parameter.save()   
            serialized_parameter = ParameterSerializer(default_parameter)
        else:
            try:
                parameters = Parameter.objects.all()
            except Parameter.DoesNotExist:
                raise Http404()
            serialized_parameter = ParameterSerializer(parameters, many=True)         
    return Response(serialized_parameter.data)  