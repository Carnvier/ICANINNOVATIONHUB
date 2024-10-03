from django.urls import path
from .views import HomePageView, AboutPageView, ServicesPageView, TeamPageView, ThematicAreasPageView, ContactUsPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about_us'), 
    path('thematic_areas/', ThematicAreasPageView.as_view(), name='thematic_areas'),
    path('services/', ServicesPageView.as_view(), name='services'), 
    path('team/', TeamPageView.as_view(), name='team'),  
    path('contact_us/', ContactUsPageView.as_view(), name= 'contact_us'),
]