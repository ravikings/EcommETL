# urls.py
from django.urls import path
from . views import MarketDataList, \
    Top5AirportsPaxByOrigin, \
    Top5AirportsPaxByDestination, \
    TopDistanceByMonth, \
    Top5AirportsFrexByOrigin, \
    Top5AirportsFrexByDestination, \
    Top5AirportsMailByOrigin, \
    Top5AirportsMailByDest, \
    Top5AirportsDistanceByOrigin, \
    Top5AirportsDistanceByDest, \
    MostPassagerByMonth, \
    MostFreightByMonth
    


urlpatterns = [
    path('list/', MarketDataList.as_view(), name="list"),
    path('top5paxorigin/',
         Top5AirportsPaxByOrigin.as_view(
             extra_context={
                 'title': "Top 5 Airports - Passengers by Origin Airport"}
         ),
         name="top5paxorigin"),
    path('top5paxdestination/',
         Top5AirportsPaxByDestination.as_view(
             extra_context={
                 'title': "Top 5 Airports - Passengers by Destination Airport"}
         ),
         name="top5paxdestination"),
    path('Top5AirportsFrexByOrigin/',
         Top5AirportsFrexByOrigin.as_view(
             extra_context={
                 'title': "Top 5 Airports - Freight by Origin Airport"}
         ),
         name="Top5AirportsFrexByOrigin"),

    path('Top5AirportsFrexByDestination/',
         Top5AirportsFrexByDestination.as_view(
             extra_context={
                 'title': "Top 5 Airports - Freight by Destination Airport"}
         ),
         name="Top5AirportsFrexByDestination"),

    path('Top5AirportsMailByOrigin/',
         Top5AirportsMailByOrigin.as_view(
             extra_context={'title': "Top 5 Airports - Mail by Origin Airport"}
         ),
         name="Top5AirportsMailByOrigin"),

    path('Top5AirportsMailByDest/',
         Top5AirportsMailByDest.as_view(
             extra_context={
                 'title': "Top 5 Airports - Mail by Destination Airport"}
         ),
         name="Top5AirportsMailByDest"),


    path('Top5AirportsDistanceByOrigin/',
         Top5AirportsDistanceByOrigin.as_view(
             extra_context={
                 'title': "Top 5 Airports - Distance by Origin Airport"}
         ),
         name="Top5AirportsDistanceByOrigin"),

    path('Top5AirportsDistanceByDest/',
         Top5AirportsDistanceByDest.as_view(
             extra_context={
                 'title': "Top 5 Airports - Distance by Destination Airport"}
         ),
         name="Top5AirportsDistanceByDest"),

# Most Passager By Month
    path('MostPassagerByMonth/',
         MostPassagerByMonth.as_view(
             extra_context={'title': "Top Passengers by Month"}
         ),
         name="MostPassagerByMonth"),

# Most freight By Month
    path('MostFreightByMonth/',
         MostFreightByMonth.as_view(
             extra_context={'title': "Top Passengers by Month"}
         ),
         name="MostFreightByMonth"),


    path('topdistance_month/',
         TopDistanceByMonth.as_view(
             extra_context={'title': "Top Distance by Month"}
         ),
         name="topdistance_month"),
]
