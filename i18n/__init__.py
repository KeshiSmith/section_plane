import json

from ..global_variables import languages_path

def load_i18n_dict():
    # read languages data from the json file.
    with open(languages_path, 'r', encoding='utf-8') as f:
        i18n_json = f.read()
    # decode dict data from json data
    i18n_dict_tmp = json.loads(i18n_json)
    # reconstuct languages dict
    i18n_dict = {}
    for locale in i18n_dict_tmp:
        locale_i18n_dict = {}
        locale_i18n_dict_tmp = i18n_dict_tmp[locale]
        for msgid in locale_i18n_dict_tmp:
            msgctxt, translation = locale_i18n_dict_tmp[msgid]
            locale_i18n_dict[(msgctxt, msgid)] = translation
        i18n_dict[locale] = locale_i18n_dict
    return i18n_dict

i18n_dict = load_i18n_dict()
