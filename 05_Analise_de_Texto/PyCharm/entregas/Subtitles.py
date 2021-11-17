import logging
import os
import re

from pysubparser import parser
from pysubparser.cleaners import brackets, formatting


def parse_filename(filename):
    rex = re.search(r"[sS]([0-9]{2})[eE]([0-9]{2})", filename)
    try:
        season, episode = rex.group(1, 2)
    except Exception as e:
        logging.error('Erro ao detectar a temporada/episódio do arquivo "{}" ({})'.format(filename, e))
        season = episode = None
    return season, episode


class Subtitles:

    def __init__(self, rootdir, encoding='latin-1'):
        self._subtitles = {}

        for dirpath, dirnames, filelist in os.walk(rootdir):
            logging.debug('Escaneando pasta {}'.format(dirpath))
            filelist.sort()
            dirnames.sort()

            for filename in filelist:
                logging.debug('Carregando arquivo de legenda "{}"'.format(filename))
                filename = os.path.join(dirpath, filename)
                season, episode = parse_filename(filename)

                data = parser.parse(filename, encoding=encoding)
                data = brackets.clean(data)
                data = formatting.clean(data)
                data = [line.text for line in data]
                self._subtitles[filename] = (season, episode, data)

    @property
    def subtitles(self):
        return [data for _, _, data in self._subtitles.values()]

    @property
    def subtitles_text(self):
        return ['\n'.join(data) for _, _, data in self._subtitles.values()]

    def __iter__(self):
        for _, _, data in self._subtitles.values():
            yield data

    def __str__(self):
        return '\n\n'.join(['\n'.join(subtitle) for subtitle in self]).replace('\x82', '')

    def __len__(self):
        return len(self._subtitles)
