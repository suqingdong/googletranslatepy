import sys
import json

import rich
import click

from googletranslatepy import (
    version_info,
    DEFAULT_URL,
    LANGUAGES,
    Translator,
    util,
)


CONTEXT_SETTINGS = dict(help_option_names=['-?', '-h', '--help'])


@click.command(
    name=version_info['prog'],
    help=click.style(version_info['desc'], italic=True, fg='cyan', bold=True),
    context_settings=CONTEXT_SETTINGS,
    no_args_is_help=True,
)
@click.argument('text')
@click.version_option(version=version_info['version'], prog_name=version_info['prog'])
@click.option('-u', '--url', help='the url of google translate', default=DEFAULT_URL, show_default=True)
@click.option('-p', '--proxies', help='the proxies url, eg. http://127.0.0.1:1080')
@click.option('-f', '--from-lang', help='the from language', default='auto', show_default=True)
@click.option('-t', '--to-lang', help='the dest language', default='zh', show_default=True)
@click.option('-s', '--timeout', help='the second of timeout', default=10, show_default=True, type=float)
@click.option('-l', '--languages', help='list all available languages', is_flag=True)
@click.option('-o', '--outfile', help='the output filename [stdout]')
def cli(**kwargs):

    if kwargs['languages']:
        rich.print_json(json.dumps(LANGUAGES))
        exit(0)

    translator = Translator(url=kwargs['url'],
                            proxies=kwargs['proxies'],
                            from_lang=kwargs['from_lang'],
                            to_lang=kwargs['to_lang'],
                            timeout=kwargs['timeout'],
                            )

    outfile = (kwargs['outfile'])
    out = util.safe_open(outfile, 'w') if outfile else sys.stdout
    with out:
        res = translator.translate(kwargs['text'])
        if res:
            out.write(res + '\n')
            if outfile:
                click.secho(f'safe file: {outfile}', fg='green', err=True)


def main():
    cli()


if __name__ == '__main__':
    main()
