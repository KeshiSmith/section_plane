import bpy

from .i18n import i18n_dict
from .global_variables import addon_name
from .ops.add_section_shader import AddSectionShaderOperator
from .ops.initialize import InitializeOperator
from .ui.section_preferences import SectionPreferences
from .ui.section_panel import SectionPanel

addon_classes = [
    AddSectionShaderOperator,
    InitializeOperator,
    SectionPreferences,
    SectionPanel
]

def register():
    # register classes
    for cls in addon_classes:
        bpy.utils.register_class(cls)
    SectionPanel.update_tab_category()
    # register translations
    bpy.app.translations.register(addon_name, i18n_dict)

def unregister():
    # unregister translations
    bpy.app.translations.unregister(addon_name)
    # unregister classes
    for cls in addon_classes[::-1]:
        bpy.utils.unregister_class(cls)
