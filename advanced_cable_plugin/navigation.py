from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices

plugin_buttons = [
    PluginMenuButton(
        link="plugins:advanced_cable_plugin:advancedcableplugin_add",
        title="Add",
        icon_class="mdi mdi-plus-thick",
    )
]

menu_items = (
    PluginMenuItem(
        link="plugins:advanced_cable_plugin:advancedcableplugin_list",
        link_text="AdvancedCablePlugin",
        buttons=plugin_buttons,
    ),
)
