from django.urls import path
from netbox.views.generic import ObjectChangeLogView

from . import models, views


urlpatterns = (
    path("advancedcableplugins/", views.AdvancedCablePluginListView.as_view(), name="advancedcableplugin_list"),
    path("advancedcableplugins/add/", views.AdvancedCablePluginEditView.as_view(), name="advancedcableplugin_add"),
    path("advancedcableplugins/<int:pk>/", views.AdvancedCablePluginView.as_view(), name="advancedcableplugin"),
    path("advancedcableplugins/<int:pk>/edit/", views.AdvancedCablePluginEditView.as_view(), name="advancedcableplugin_edit"),
    path("advancedcableplugins/<int:pk>/delete/", views.AdvancedCablePluginDeleteView.as_view(), name="advancedcableplugin_delete"),
    path(
        "advancedcableplugins/<int:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="advancedcableplugin_changelog",
        kwargs={"model": models.AdvancedCablePlugin},
    ),
)
