import bpy
from  bpy.props import StringProperty

from ..global_variables import (
    addon_name,
    default_tab_category
)
from .section_panel import SectionPanel

class SectionPreferences(bpy.types.AddonPreferences):
    bl_idname = addon_name

    def __update_category(self, context):
        if self.tab_category == "Tool":
            self.tab_category = default_tab_category
        SectionPanel.update_tab_category()

    tab_category : StringProperty(
        name = "Tab Category",
        description="Customize the category of the addon panel",
        default = default_tab_category,
        update = __update_category
    )

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "tab_category")