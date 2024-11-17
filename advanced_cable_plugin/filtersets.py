from netbox.filtersets import NetBoxModelFilterSet
from .models import AdvancedCablePlugin


# class AdvancedCablePluginFilterSet(NetBoxModelFilterSet):
#
#     class Meta:
#         model = AdvancedCablePlugin
#         fields = ['name', ]
#
#     def search(self, queryset, name, value):
#         return queryset.filter(description__icontains=value)
