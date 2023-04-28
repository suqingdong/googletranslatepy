import textwrap

import requests
import deep_translator


class Translator(object):
    """
        https://translate.google.cn no longer provides service,
        so we use https://translate.google.com with proxies instead.

        >>> from googletranslatepy import Translator
        >>> translator = Translator(proxies='http://127.0.0.1:10809')
        >>> translator.translate('Life is short, you need Python!')
    """

    def __init__(self, proxies=None, source='auto', target='zh-CN', **kwargs):
        self.proxies = {'https': proxies} if isinstance(proxies, str) else proxies
        self.trans = deep_translator.GoogleTranslator(
            source=source,
            target=target,
            proxies=self.proxies,
        )

    def translate(self, text, **kwargs):
        """
            the length of characters is limited within 5000,
        """
        text_list = textwrap.wrap(
            text,
            width=4999,
            break_long_words=False,
            break_on_hyphens=False,
            drop_whitespace=False,
            replace_whitespace=False,
        )
        try:
            res = ' '.join(self.trans.translate(t, **kwargs) for t in text_list)
            return res
        except Exception as e:
            print(e)
            return False

    def check_proxies(self, timeout=5):
        url = self.trans._base_url
        try:
            return requests.head(url, proxies=self.proxies, timeout=timeout)
        except Exception:
            return False
