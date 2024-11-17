from django import forms
from ipam.models import Prefix
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from utilities.forms.fields import CommentField, DynamicModelChoiceField

from .models import AdvancedCablePlugin


class AdvancedCablePluginForm(NetBoxModelForm):
    class Meta:
        model = AdvancedCablePlugin
        fields = ("name", "tags")
