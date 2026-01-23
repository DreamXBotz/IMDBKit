import logging

logger = logging.getLogger(__name__)

SUPPORTED_LOCALES = ("en", "fr-ca", "fr", "hi", "de", "it", "es", "pt", "es-es")
DEFAULT_LOCALE = "en"
_configured_locale = None


def set_locale(locale: str):
    global _configured_locale
    _configured_locale = locale


def _normalize_locale(lcl: str):
    if lcl not in SUPPORTED_LOCALES:
        logger.warning("Locale '%s' is not supported. Using '%s'", lcl, DEFAULT_LOCALE)
        return DEFAULT_LOCALE
    return lcl


def get_locale():
    lcl = _configured_locale or DEFAULT_LOCALE
    lcl = _normalize_locale(lcl)
    return "" if lcl == DEFAULT_LOCALE else lcl


def _retrieve_url_lang(locale=None):
    lcl = locale or _configured_locale or DEFAULT_LOCALE
    lcl = _normalize_locale(lcl)
    return "" if lcl == DEFAULT_LOCALE else lcl
