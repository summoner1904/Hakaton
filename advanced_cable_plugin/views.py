from django.db.models import Count

from netbox.views import generic
from . import filtersets, forms, models, tables


class AdvancedCablePluginView(generic.ObjectView):
    queryset = models.AdvancedCablePlugin.objects.all()


class AdvancedCablePluginListView(generic.ObjectListView):
    queryset = models.AdvancedCablePlugin.objects.all()
    table = tables.AdvancedCablePluginTable


class AdvancedCablePluginEditView(generic.ObjectEditView):
    queryset = models.AdvancedCablePlugin.objects.all()
    form = forms.AdvancedCablePluginForm


class AdvancedCablePluginDeleteView(generic.ObjectDeleteView):
    queryset = models.AdvancedCablePlugin.objects.all()
