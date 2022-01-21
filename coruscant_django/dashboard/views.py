from django.views import View
from django.views.generic import ListView

from coruscant_django.servers.models import Server


class DashboardView(ListView):
    model = Server
    context_object_name = 'servers_list'
    template_name = 'dashboard/dashboard.html'        