import json
from pathlib import Path

from .translator import Translator
from .language import LANGUAGES


DEFAULT_URL = 'https://translate.google.com'

BASE_DIR = Path(__file__).resolve().parent
version_info = json.load(BASE_DIR.joinpath('version.json').open())

__version__ = version_info['version']
