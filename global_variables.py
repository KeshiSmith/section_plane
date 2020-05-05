# global variables
addon_name = __package__
default_tab_category = "Section"

# global path
from . import util
root_path = util.get_file_path(__file__)
languages_path = root_path + "\\i18n\\languages.json"
lib_path = root_path + "\\lib\\section_lib.blend"

# libraries name
section_collection_name = "SP_Section_Tools"
section_material_name = "SP_Default_Material"
section_node_group_name = "SP_Section_Shader"
