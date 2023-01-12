from constance import config
from django.conf import settings
from django.middleware.csrf import get_token
from django.templatetags.static import static
from django.urls import reverse
from django.utils import translation
from django.utils.timezone import now
from jinja2 import Environment
from markdown import markdown

from utils.forms import add_attr

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
        'attr': add_attr,
        'date': lambda date, format: date.strftime(format),
        'md': lambda text: markdown(text),  # TODO: better protection
    },
}


def environment(**options):
    env = Environment(**options, extensions=['jinja2.ext.i18n'])
    env.autoescape = True
    env.install_gettext_translations(translation, newstyle=True)

    env.globals.update(context['globals'])
    env.filters.update(context['filters'])

    return env
