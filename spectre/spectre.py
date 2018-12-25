from django.conf import settings

SPECTRE_DEFAULTS = {
    "css_url": {
        "url": "https://unpkg.com/spectre.css/dist/spectre.min.css"
    },

}

# Start with a copy of default settings
SPECTRE = SPECTRE_DEFAULTS.copy()

# Override with user settings from settings.py
SPECTRE.update(getattr(settings, "SPECTRE", {}))


def get_spectre_setting(setting, default=None):
    """
    read settings
    :param setting:
    :param default:
    :return: spectre setting
    """
    return SPECTRE.get(setting, default)


def css_url():
    return get_spectre_setting("css_url")

