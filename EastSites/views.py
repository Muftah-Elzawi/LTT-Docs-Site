from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .models import Site
import folium


def index(request):
    context = {}
    query = ''
    if request.GET:
        query = request.GET['q']
        context['query'] = str(query)

    bgzsites = Site.objects.get_queryset()
    print(bgzsites)

    if len(bgzsites):

        m = folium.Map(width=600, height=300,location=[32.098084,20.091047], zoom_start=13)
        for i in range(0,len(bgzsites)):
            folium.Marker([bgzsites[i].siteLatitude, bgzsites[i].siteLongitude], popup=bgzsites[i].siteName).add_to(m)
        m = m._repr_html_()
    context = {
        'bgzsites':bgzsites,
        'MAP':m
    }
    return render(request, 'home.html',context)


def city(request, cityName):
    cityName = str(cityName)
    print(cityName)
    citySites = Site.objects.filter(siteCity=cityName)
    # except Eastsites.DoesNotExist:
    print(citySites[0].siteLatitude)
    m = folium.Map(width=600, height=300,location=[citySites[0].siteLatitude, citySites[0].siteLongitude], zoom_start=13)
    # tooltip = 'Click For More Info'
    for i in range(0,len(citySites)):
        folium.Marker([citySites[i].siteLatitude, citySites[i].siteLongitude], popup=citySites[i].siteName).add_to(m)
    m = m._repr_html_()
    context = {
        'citySites':citySites,
        'MAP':m
    }
    return render(request, "cities.html", context)



def site(request, pk):
    print(pk)
    singleSite = Site.objects.filter(id=pk)
    print(singleSite[0])
    m = folium.Map(width=600, height=300,location=[singleSite[0].siteLatitude, singleSite[0].siteLongitude], zoom_start=13)
    folium.Marker([singleSite[0].siteLatitude, singleSite[0].siteLongitude], popup=singleSite[0].siteName).add_to(m)
    m = m._repr_html_()
    context = {
        'singleSite': singleSite[0],
        'MAP':m
    }
    return render(request, "single.html",context)