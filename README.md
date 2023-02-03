# Google Translate Client with `deep-translator`

## Install

```bash
python3 -m pip install googletranslatepy
```

## Usage

***Python***

```python
from googletranslatepy import Translator

translator = Translator(proxies='http://127.0.0.1:10809')

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
```
