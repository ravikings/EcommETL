# Create your views here.
import pdb
from django.views.generic import ListView
from django.db.models import Max, Sum

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
