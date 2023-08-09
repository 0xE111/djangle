from bs4 import BeautifulSoup
from django.conf import settings
from django.core.mail import send_mail as django_send_mail
from django.template import engines


def send_mail(
    template: str,
    context: dict,
    recipients: list[str],
    sender: str = settings.SERVER_EMAIL,
    *args,
    **kwargs,
):
    context.update({
        'template': template,
    })
    engine = engines['jinja2']
    subject = engine.from_string('{% extends template %}{% block content -%}{% endblock %}').render(context).strip('\n ')
    message = engine.from_string('{% extends template %}{% block subject -%}{% endblock %}').render(context).strip('\n ')
    django_send_mail(
        subject=subject,
        message=BeautifulSoup(message, features='html.parser').get_text(),
        html_message=message,
        from_email=sender,
        recipient_list=recipients,
        *args,
        **kwargs,
    )


def mail_admins(template, context, *args, **kwargs):
    send_mail(template, context, [email for _, email in settings.ADMINS], *args, **kwargs)


def mail_managers(template, context, *args, **kwargs):
    send_mail(template, context, [email for _, email in settings.MANAGERS], *args, **kwargs)
