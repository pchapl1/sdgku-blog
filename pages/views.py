
from django.views.generic import TemplateView
from .models import *

class Home(TemplateView):
    template_name = 'home.html'


class About(TemplateView):
    template_name = 'about.html'
