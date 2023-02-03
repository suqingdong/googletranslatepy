# Google Translate Client with `deep-translator`

## Install

```bash
python3 -m pip install googletranslatepy
```

## Usage

***Python***

```python
from googletranslatepy import Translator

# use a http proxies
translator = Translator(proxies='http://127.0.0.1:10809')

# use a socks5 proxies
translator = Translator(proxies='socks5://127.0.0.1:10808')

translator.translate('Life is short, you need Python!')
# '人生苦短，你需要 Python！'
```

***CMD***

```bash
googletranslate --help

# translate a string text
googletranslate -p http://127.0.0.1:10809 'Life is short, you need Python!'

# translate a file
googletranslate -p http://127.0.0.1:10809 README.md

# set proxies to env
GOOGLE_PROXIES=http://127.0.0.1:10809 googletranslate 'hello world'

# or add to: ~/.bash_profile
export GOOGLE_PROXIES=http://127.0.0.1:10809
# and then use it directly
googletranslate 'hello world'
```
