import bpy
from bpy.app.translations import pgettext_iface as iface

from ..global_variables import (
    addon_name,
    default_tab_category,
    section_collection_name
)

from ..ops.add_section_shader import AddSectionShaderOperator
from ..ops.initialize import InitializeOperator

class SectionPanel(bpy.types.Panel):
    """ The addon panel in the sidebar """
    bl_idname = "OBJECT_PT_section_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = default_tab_category
    bl_label = "Section Plane 1.0.0"

    @classmethod
    def update_tab_category(cls):
        cls.bl_category = \
            bpy.context.preferences.addons[addon_name].preferences.tab_category
        bpy.utils.unregister_class(SectionPanel)
        bpy.utils.register_class(SectionPanel)

    @classmethod
    def poll(cls, context):
        return context.mode == 'OBJECT'
    
    def draw(self, context):
        layout = self.layout
        # initialize button
        row = layout.row()
        row.active = section_collection_name not in bpy.data.collections.keys()
        row.operator(InitializeOperator.bl_idname)
        # other operators
        if section_collection_name in bpy.data.collections.keys():
            layout.operator(AddSectionShaderOperator.bl_idname)
