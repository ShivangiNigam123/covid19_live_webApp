from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "874934c2fbmsh645324ca5946ed4p172ed9jsn66a781caa5ae",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()

# print(response.text)
# Create your views here.
def index(request):
    mylist=[]
    noofresults = int(response['results'])
    for x in range(0,noofresults):
         mylist.append(response['response'][x]['country'])
    if request.method == "POST" :
      selectedcountry= request.POST['selectedcountry']
       # noofresults = int(response['results'])
      for x in range(0,noofresults):
          if selectedcountry == response['response'][x]['country']:
              new = response['response'][x]['cases']['new']
              active = response['response'][x]['cases']['active']
              critical = response['response'][x]['cases']['critical']
              recovered = response['response'][x]['cases']['recovered']
              total = response['response'][x]['cases']['total']
              newdeaths = response['response'][x]['deaths']['new']
              totaldeaths = response['response'][x]['deaths']['total']

      context = {'selectedcountry': selectedcountry, 'mylist' : mylist, 'new' : new, 'active' : active, 'critical' : critical, 'recovered' : recovered, 'total' : total, 'newdeaths' : newdeaths, 'totaldeaths' : totaldeaths }
      return render(request, 'covidapp/index.html', context)
    noofresults = int(response['results'])
    mylist=[]
    for x in range(0,noofresults):
       mylist.append(response['response'][x]['country'])
       context = {'mylist' : mylist}
       return render(request, 'covidapp/index.html', context)
