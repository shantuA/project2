from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def sachivji(request):
    return HttpResponse("<h1><center>Jitendra Kumar<center></h1> <h2><center>Jitendra Kumar is an Indian actor."
" He is best known for his role of Jitu in TVF Pitchers, Jeetu Bhaiya in the series"
" Kota Factory, and for his roles SACHIVJI in Amazon Prime's comedy series Panchayat. <center></h2>" )

def banrakas(request):
    return HttpResponse("<h1><center>Durgesh Kumar<center></h1><h2><center>Durgesh Kumar is an Indian actor. "
" He is best known for his role of BANRAKAS in Amazon Prime's comedy series Panchayat.<center></h2>" )

def binod(request):
    return HttpResponse("<h1><center>Ashok pathak<center></h1><h2><center>Ashok pathak is an Indian actor. "
" He is best known for his role of BINOD in Amazon Prime's comedy series Panchayat.<center></h2>" )