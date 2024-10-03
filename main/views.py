from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about_us.html'

class ThematicAreasPageView(TemplateView):
    template_name = 'thematic_areas.html'

class ServicesPageView(TemplateView):
    template_name = 'services.html'

class TeamPageView(TemplateView):
    template_name = 'team.html'

class ContactUsPageView(TemplateView):
    template_name = 'contact_us.html'