from django.shortcuts import render, redirect,get_object_or_404
from .models import*
from rest_framework import generics
from .serializers import *

def home(request):
    return render(request, 'index.html')

def home2(request):
    societe=Societe.objects.all()
    context={
        'societe':societe
    }
    return render(request, 'index2.html', context)

def reserve(request, societe_id):
    
    societe =get_object_or_404(Societe, id=societe_id)
    
    time=Heure_d.objects.all()
    destination=Destination.objects.all()
    context={
        
        'societe':societe,
        'time':time,
        'destination':destination,
    }
    return render(request, 'reservation.html', context)

def addreserve(request, societe_id):
    societe = Societe.objects.get(id=societe_id)
    time=Heure_d.objects.all()
    destination=Destination.objects.all()
    if request.method=="POST":
        societe_nom = [x.nom for x in Societe.objects.all()]
        societe_ids=[Societe.objects.get(id=societe_id)]
        
        nom = request.POST.get('nom') 
        prenom = request.POST.get('prenom')
        date=request.POST.get('date')
        time_pk=request.POST.get('time')
        time=Heure_d.objects.get(pk=time_pk)
        tel = request.POST.get('tel')
        num_trans=request.POST.get('num_trans')
        destination_pk=request.POST.get('destination')
        destination=Destination.objects.get(pk=destination_pk)
        
        reservation = Reservations.objects.create(nom=nom, prenom=prenom,date=date,
                                                        time=time, tel=tel, num_trans=num_trans ,destination=destination)
        
        reservation.societe.add(Societe.objects.get(id=societe_id))
        reservation.save()
        return redirect('home2')
    return render(request, 'reservation.html',{'societe':societe})

class SocieteListView(generics.ListAPIView):
    queryset = Societe.objects.all()
    serializer_class = SocieteSerializer
    
class ReservationsListView(generics.ListAPIView):
    queryset = Reservations.objects.all()
    serializer_class = ReservationsSerializer

class HeurListView(generics.ListAPIView):
    queryset = Heure_d.objects.all()
    serializer_class = HeurSerializer
    
class DetinationListView(generics.ListAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer