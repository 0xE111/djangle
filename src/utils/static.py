import hashlib
from functools import lru_cache
from typing import Iterable

from django.contrib.staticfiles import finders
from django.contrib.staticfiles.storage import staticfiles_storage


class StaticFilesException(Exception):
    pass


def iterfile(file_path: str, block_size: int = 65536) -> Iterable[bytes]:
    """ Reads file by chunks """
    with open(file_path, 'rb') as file:
        block = file.read(block_size)
        while len(block) > 0:
            yield block
            block = file.read(block_size)


def hex_hash(file_path: str) -> str:
    """ Calculates hash of file contents, in as hexdigest string """
    hasher = hashlib.sha256()
    for block in iterfile(file_path):
        hasher.update(block)

    return hasher.hexdigest()


@lru_cache()
def static(file_path: str) -> str:
    """
    Given relative path to any static file, produces url to that file with a `hash` parameter.
    When file updates, the hash is updated too, thus forcing browser to reload the file.

    :param file_path: relative path to static file
    :return: url to static file with hash string
    """
    file = finders.find(file_path)
    if not file:
        raise StaticFilesException('File not found: {}'.format(file_path))

    return '{url}?hash={hash}'.format(
        url=staticfiles_storage.url(file_path),
        hash=hex_hash(file)[:8],
    )
