import requests
from django.conf import settings
import logging


log = logging.getLogger(__name__)


def notify(message: str):
    log.info('Notification: %s', message)

    if not (url := settings.NOTIFICATIONS_URL):
        return

    try:
        response = requests.post(url, data=message.encode('utf-8'), timeout=5)
        response.raise_for_status()
    except Exception:
        log.exception('Could not send notification to %s', url)
