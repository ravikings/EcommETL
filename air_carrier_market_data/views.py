# Create your views here.
import pdb
from django.views.generic import ListView
from django.db.models import Avg, Max, Min, Sum

from . models import MarketData

class MarketDataList(ListView):
    model = MarketData

# What are the top 5 airports in terms of: Total passengers by origin
class Top5AirportsPaxByOrigin(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('orig_iata_code','orig_city_name') \
                        .annotate(total_pax=Sum('passengers')) \
                        .order_by('-total_pax')[0:5]
    template_name="rankorder_list_origin.html"

# What are the top 5 airports in terms of: Total passengers by destination
class Top5AirportsPaxByDestination(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('dest_iata_code','dest_city_name') \
                                 .annotate(total_pax=Sum('passengers')) \
                                 .order_by('-total_pax')[0:5]
    template_name="rankorder_list_destination.html"

# What are the top 5 airports in terms of: Total freight by origin: 
class Top5AirportsFrexByOrigin(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('orig_iata_code','orig_city_name') \
                                 .annotate(total_frex=Sum('freight')) \
                                 .order_by('-total_frex')[0:5]
    template_name="ranker_list_frex.html"

# What are the top 5 airports in terms of: Total freight by destination
class Top5AirportsFrexByDestination(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('dest_iata_code','dest_city_name') \
                                 .annotate(total_dfrex=Sum('freight')) \
                                 .order_by('-total_dfrex')[0:5]
    template_name="ranker_list_dest_freight.html"

# What are the top 5 airports in terms of: Total mail by origin
class Top5AirportsMailByOrigin(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('orig_iata_code','orig_city_name') \
                                 .annotate(total_mail=Sum('mail')) \
                                 .order_by('-total_mail')[0:5]
    template_name="ranker_list_origin_mail.html"

# What are the top 5 airports in terms of: Total mail by destination
class Top5AirportsMailByDest(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('dest_iata_code','dest_city_name') \
                                 .annotate(total_mail=Sum('mail')) \
                                 .order_by('-total_mail')[0:5]
    template_name="ranker_list_dest_mail.html" 

# What are the top 5 airports in terms of: Total distance by origin
class Top5AirportsDistanceByOrigin(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('orig_iata_code','orig_city_name') \
                                 .annotate(total_dest=Sum('distance')) \
                                 .order_by('-total_dest')[0:5]
    template_name="ranker_list_origin_distance.html"


# What are the top 5 airports in terms of: Total destance by destination
class Top5AirportsDistanceByDest(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('dest_iata_code','dest_city_name') \
                                 .annotate(total_dest=Sum('distance')) \
                                 .order_by('-total_dest')[0:5]
    template_name="ranker_list_dest_dest_mail.html" 

# Which airport reported the most passengers by month?
class MostPassagerByMonth(ListView):
    context_object_name = "airport_list"
    template_name="rankorder_most_passenger_month.html"

    def get_queryset(self):

        month_list = []

        # pdb.set_trace()

        # there are six months worth of data
        # not good ultimately as this is a "hard-coded" fore-knowledge of the data
        for month in range(1,7):
            queryset = MarketData.objects \
                .values('orig_iata_code',
                        'orig_city_name',
                        'dest_iata_code',
                        'dest_city_name',
                        'month') \
                .filter(month__exact=month) \
                .annotate(total_passengers=Max('passengers')) \
                .order_by('-total_passengers')[0:1]
            
            # off by one error for assignment

            month_list.append(queryset)

        # return list
        return month_list


# Which airline reported the most freight carried?
class MostFreightByMonth(ListView):
    context_object_name = "airport_list"
    template_name="rankorder_most_freight_month.html"

    def get_queryset(self):

        month_list = []

        # pdb.set_trace()

        # there are six months worth of data
        # not good ultimately as this is a "hard-coded" fore-knowledge of the data
        for month in range(1,7):
            queryset = MarketData.objects \
                .values('orig_iata_code',
                        'orig_city_name',
                        'dest_iata_code',
                        'dest_city_name',
                        'month') \
                .filter(month__exact=month) \
                .annotate(total_freight=Max('freight')) \
                .order_by('-total_freight')[0:1]
            
            # off by one error for assignment

            month_list.append(queryset)

        # return list
        return month_list


# Which airport reported the longest distance by month?
class TopDistanceByMonth(ListView):
    context_object_name = "airport_list"
    template_name="rankorder_list_origin_distance_month.html"

    def get_queryset(self):

        month_list = []

        # pdb.set_trace()

        # there are six months worth of data
        # not good ultimately as this is a "hard-coded" fore-knowledge of the data
        for month in range(1,7):
            queryset = MarketData.objects \
                .values('orig_iata_code',
                        'orig_city_name',
                        'dest_iata_code',
                        'dest_city_name',
                        'month') \
                .filter(month__exact=month) \
                .annotate(total_distance=Max('distance')) \
                .order_by('-total_distance')[0:1]
            
            # off by one error for assignment

            month_list.append(queryset)

        # return list
        return month_list


# Which airline reported the most passengers carried?
class MostPassengersCarried(ListView):
    context_object_name = "airport_list"
    template_name="rankorder_most_passenger.html"

    def get_queryset(self):

        month_list = []

        # pdb.set_trace()

        # there are six months worth of data
        # not good ultimately as this is a "hard-coded" fore-knowledge of the data
        for month in range(1,2):
            queryset = MarketData.objects \
                .values('orig_iata_code',
                        'orig_city_name',
                        'dest_iata_code',
                        'dest_city_name',
                        'month') \
                .filter(month__exact=month) \
                .annotate(total_passengers=Max('passengers')) \
                .order_by('-total_passengers')[0:1]
            
            # off by one error for assignment

            month_list.append(queryset)

        # return list
        return month_list


# Which airline reported the most mail carried?
class MostMailCarried(ListView):
    context_object_name = "airport_list"
    template_name="rankorder_most_mail.html"

    def get_queryset(self):

        month_list = []

        # pdb.set_trace()

        # there are six months worth of data
        # not good ultimately as this is a "hard-coded" fore-knowledge of the data
        for month in range(1,2):
            queryset = MarketData.objects \
                .values('orig_iata_code',
                        'orig_city_name',
                        'dest_iata_code',
                        'dest_city_name',
                        'month') \
                .filter(month__exact=month) \
                .annotate(total_mail=Max('mail')) \
                .order_by('-total_mail')[0:1]
            
            # off by one error for assignment

            month_list.append(queryset)

        # return list
        return month_list


# Which airport reported the longest distance by month?
class LongestDistance(ListView):
    context_object_name = "airport_list"
    template_name="LongestDistance_flight.html"

    def get_queryset(self):

        month_list = []

        # pdb.set_trace()

        # there are six months worth of data
        # not good ultimately as this is a "hard-coded" fore-knowledge of the data
        for month in range(0,2):
            queryset = MarketData.objects \
                .values('orig_iata_code',
                        'orig_city_name',
                        'dest_iata_code',
                        'dest_city_name',
                        'month') \
                .filter(month__exact=month) \
                .annotate(total_dix=Max('distance')) \
                .order_by('-total_dix')[0:1]
            
            # off by one error for assignment

            month_list.append(queryset)

        # return list
        return month_list

# Find the average number of passengers for flights into: LAX (Los Angeles)
class AverPassengerslAXAirport(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('dest_iata_code','dest_city_name') \
                                 .annotate(total_Pass=Avg('passengers')) \
                                 .filter(dest_iata_code='LAX') \
                                 .order_by('-total_Pass')
    template_name="average_paasenger_by_LAXAirport.html"

# Find the average number of passengers for flights into: SFO (San Francisco)
class AverPassengersSFOAirport(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('dest_iata_code','dest_city_name') \
                                 .annotate(total_Pass=Avg('passengers')) \
                                 .filter(dest_iata_code='SFO') \
                                 .order_by('-total_Pass')
    template_name="average_paasenger_by_SFOAirport.html"


 # Find the average number of passengers for flights into: DFW (Dallas-Fort Worth)
class AverPassengersDFWAirport(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('dest_iata_code','dest_city_name') \
                                 .annotate(total_Pass=Avg('passengers')) \
                                 .filter(dest_iata_code='DFW') \
                                 .order_by('-total_Pass')
    template_name="average_paasenger_by_DFWAirport.html"

# Find the average number of passengers for flights into: ATL (Atlanta)
class AverPassengersATLAirport(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('dest_iata_code','dest_city_name') \
                                 .annotate(total_Pass=Avg('passengers')) \
                                 .filter(dest_iata_code='ATL') \
                                 .order_by('-total_Pass')
    template_name="AverPassengersATLAirport.html"

# Find the average number of passengers for flights into: ATL (Atlanta)
class AverPassengersORDAirport(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('dest_iata_code','dest_city_name') \
                                 .annotate(total_Pass=Avg('passengers')) \
                                 .filter(dest_iata_code='ATL') \
                                 .order_by('-total_Pass')
    template_name="AverPassengersORDAirport.html"

# Find the average volume of freight for flights departing:  MIA (Miami)
class AverfreightMIAAirport(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('dest_iata_code','dest_city_name') \
                                 .annotate(total_Pass=Avg('freight')) \
                                 .filter(dest_iata_code='MIA') \
                                 .order_by('-total_Pass')
    template_name="AverfreightMIAAirport.html"

# Find the average volume of freight for flights departing: MEM (Memphis)
class AverFreightMEMAirport(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('dest_iata_code','dest_city_name') \
                                 .annotate(total_Pass=Avg('freight')) \
                                 .filter(dest_iata_code='MEM') \
                                 .order_by('-total_Pass')
    template_name="AverFreightMEMAirport.html"

# Find the average volume of freight for flights departing: JFK (New York JFK)
class AverFreightJFKAirport(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('dest_iata_code','dest_city_name') \
                                 .annotate(total_Pass=Avg('freight')) \
                                 .filter(dest_iata_code='JFK') \
                                 .order_by('-total_Pass')
    template_name="AverFreightJFKAirport.html"

 # Find the average volume of freight for flights departing: ANC (Anchorage)
class AverFreightANCAirport(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('dest_iata_code','dest_city_name') \
                                 .annotate(total_Pass=Avg('freight')) \
                                 .filter(dest_iata_code='ANC') \
                                 .order_by('-total_Pass')
    template_name="AverFreightANCAirport.html"

 # Find the average volume of freight for flights departing: SDF (Louisville)
class AverFreightSDFAirport(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('dest_iata_code','dest_city_name') \
                                 .annotate(total_Pass=Avg('freight')) \
                                 .filter(dest_iata_code='SDF') \
                                 .order_by('-total_Pass')
    template_name="AverFreightSDFAirport.html"

# 	What city pairs represent the most freight carried for the longest distance?
class MaxFreight(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('dest_iata_code','dest_city_name') \
                                 .annotate(total_Pass=Max('freight')) \
                                 .order_by('-total_Pass')[0:1]
    template_name="MaxFreight.html"

# What city pairs represent the most mail carried for the shortest distance?
class MinFreight(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('dest_iata_code','dest_city_name') \
                                 .annotate(total_Pass=Min('freight')) \
                                 .order_by('-total_Pass')[0:1]
    template_name="MinFreight.html"




