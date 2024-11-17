"""Top-level package for Advanced_Cabel_Plugin."""

__author__ = """Timur Azimov"""
__email__ = "serjasum1994@icloud.com"
__version__ = "1.0.0"


from netbox.plugins import PluginConfig


class AdvancedCablePluginConfig(PluginConfig):
    name = "advanced_cable_plugin"
    verbose_name = "Advanced_Cabel_Plugin"
    description = "A NetBox plugin to enhance cable functionality with fiber types and modules"
    version = "version"
    base_url = "advanced_cable_plugin"


config = AdvancedCablePluginConfig
