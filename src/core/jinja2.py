from constance import config
from django.conf import settings
from django.middleware.csrf import get_token
from django.urls import reverse
from django.utils import translation
from django.utils.timezone import now
from utils.static import static

from jinja2 import Environment

context = {
    'globals': {
        'DEBUG': settings.DEBUG,
        'config': config,
        'LANG': settings.LANGUAGE_CODE,

        'static': static,
        'csrf_token': get_token,
        'url': reverse,
        'now': now,
    },
    'filters': {
    },
}


def environment(**options):
    env = Environment(**options, extensions=['jinja2.ext.i18n'])
    env.autoescape = True
    env.install_gettext_translations(translation, newstyle=True)

    env.globals.update(context['globals'])
    env.filters.update(context['filters'])

    return env
