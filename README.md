# Google Translate Client with `itranslate`

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
# '生活很短，您需要Python！'
```

***CMD***

```bash
gtranspy --help

gtranspy 'hello world!' -p http://127.0.0.1:10809

gtranspy 'hello world!' -p http://127.0.0.1:10809 -o result.txt
```
