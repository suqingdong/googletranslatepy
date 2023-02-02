import textwrap
import functools

import itranslate


class Translator(object):
    """
        https://translate.google.cn no longer provides service,
        so we use https://translate.google.com with proxies instead.

        >>> from googletranslatepy import Translator
        >>> translator = Translator(proxies='http://127.0.0.1:10809')
        >>> translator.translate('hello world!')
    """

    def __init__(self,
                 url='https://translate.google.com',
                 proxies=None,
                 timeout=10,
                 from_lang='auto',
                 to_lang='zh',
                 **kwargs):
        self.itrans = functools.partial(
            itranslate.itranslate,
            url=url,
            from_lang=from_lang,
            to_lang=to_lang,
            proxies=proxies,
            timeout=timeout,
            **kwargs,
        )

    def translate(self, text):
        """
            the length of characters is limited within 5000,
        """
        text_list = textwrap.wrap(
            text,
            width=5000,
            break_long_words=False,
            break_on_hyphens=False,
            drop_whitespace=False,
            replace_whitespace=False,
        )
        try:
            res = ' '.join(self.itrans(t) for t in text_list)
            return res
        except Exception:
            return False


if __name__ == '__main__':
    translator = Translator(proxies='http://127.0.0.1:10809')
    translator.translate('hello world!')
