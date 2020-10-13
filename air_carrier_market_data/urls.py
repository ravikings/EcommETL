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
    MostFreightByMonth, \
    MostPassengersCarried, \
    MostMailCarried, \
    LongestDistance, \
    AverPassengerslAXAirport, \
    AverPassengersSFOAirport, \
    AverPassengersDFWAirport, \
    AverPassengersATLAirport, \
    AverPassengersORDAirport, \
    AverfreightMIAAirport, \
    AverFreightMEMAirport, \
    AverFreightJFKAirport, \
    AverFreightANCAirport, \
    AverFreightSDFAirport, \
    MaxFreight, \
    MinFreight

    


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

# URL airline reported the most passengers carried?
    path('MostPassengersCarried/',
         MostPassengersCarried.as_view(
             extra_context={'title': "Most Passenger"}
         ),
         name="MostPassengersCarried"),


# URL airline reported the most mail carried?
    path('MostMailCarried/',
         MostMailCarried.as_view(
             extra_context={'title': "Most Mail"}
         ),
         name="MostMailCarried"),

# URL airline reported the most longest flight distance??
   path('LongestDistance/',
         LongestDistance.as_view(
             extra_context={'title': "Most Mail"}
         ),
         name="LongestDistance"),


# Find the average number of passengers for flights into: LAX (Los Angeles)
   path('AverPassengerslAXAirport/',
         AverPassengerslAXAirport.as_view(
             extra_context={'title': "average number of passengers into: LAX (Los Angeles) "}
         ),
         name="AverPassengerslAXAirport"),

# Find the average number of passengers for flights into: SFO (San Francisco)
   path('AverPassengersSFOAirport/',
         AverPassengersSFOAirport.as_view(
             extra_context={'title': "average number of passengers into: SFO (San Francisco) "}
         ),
         name="AverPassengersSFOAirport"),

# Find the average number of passengers for flights into: DFW (Dallas-Fort Worth)
   path('AverPassengersDFWAirport/',
         AverPassengersDFWAirport.as_view(
             extra_context={'title': "average number of passengers into:  DFW (Dallas-Fort Worth) "}
         ),
         name="AverPassengersDFWAirport"),

# Find the average number of passengers for flights into: ATL (Atlanta)
   path('AverPassengersATLAirport/',
         AverPassengersATLAirport.as_view(
             extra_context={'title': "average number of passengers into:  ATL (Atlanta)"}
         ),
         name="AverPassengersATLAirport"),

# Find the average number of passengers for flights into: ORD (Chicago)
   path('AverPassengersORDAirport/',
         AverPassengersORDAirport.as_view(
             extra_context={'title': "average number of passengers into: ORD (Chicago)"}
         ),
         name="AverPassengersORDAirport"),

# URL average volume of freight for flights departing:  MIA (Miami)
   path('AverfreightMIAAirport/',
         AverfreightMIAAirport.as_view(
             extra_context={'title': "average number of freights into: MIA (Miami)"}
         ),
         name="AverfreightMIAAirport"),

# URL average volume of freight for flights departing: MEM (Memphis)
   path('AverFreightMEMAirport/',
         AverFreightMEMAirport.as_view(
             extra_context={'title': "average number of freights into: MEM (Memphis)"}
         ),
         name="AverFreightMEMAirport"),

# URL Find the average volume of freight for flights departing: JFK (New York JFK)
  path('AverFreightJFKAirport/',
         AverFreightJFKAirport.as_view(
             extra_context={'title': "average number of freights into: JFK (New York JFK)"}
         ),
         name="AverFreightJFKAirport"),
    
# URL Find the average volume of freight for flights departing: ANC (Anchorage)
 path('AverFreightANCAirport/',
         AverFreightANCAirport.as_view(
             extra_context={'title': "average number of freights into: ANC (Anchorage)"}
         ),
         name="AverFreightANCAirport"),
    
# Find the average volume of freight for flights departing: SDF (Louisville)
 path('AverFreightSDFAirport/',
         AverFreightSDFAirport.as_view(
             extra_context={'title': "average number of freights into: SDF (Louisville)"}
         ),
         name="AverFreightSDFAirport"),

# 	What city pairs represent the most freight carried for the longest distance?
 path('MaxFreight/',
         MaxFreight.as_view(
             extra_context={'title': "City representing the most freight carried for the longest distance"}
         ),
         name="MaxFreight"),

# What city pairs represent the most mail carried for the shortest distance?
 path('MinFreight/',
         MinFreight.as_view(
             extra_context={'title': "City representing the most freight carried for the Shortest distance"}
         ),
         name="MinFreight"),

    path('topdistance_month/',
         TopDistanceByMonth.as_view(
             extra_context={'title': "Top Distance by Month"}
         ),
         name="topdistance_month"),
]
