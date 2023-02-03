import os
import sys
import json

import rich
import click
import deep_translator

from googletranslatepy import (
    util,
    Translator,
    version_info,
)


CONTEXT_SETTINGS = dict(help_option_names=['-?', '-h', '--help'])
EPILOG = click.style(
    'contact: {author} <{author_email}>',
    fg='bright_white',
    italic=True,
    bold=True
).format(**version_info)


@click.command(
    name=version_info['prog'],
    help=click.style(version_info['desc'], italic=True, fg='cyan', bold=True),
    context_settings=CONTEXT_SETTINGS,
    no_args_is_help=True,
    epilog=EPILOG,
)
@click.argument('text')
@click.version_option(version=version_info['version'], prog_name=version_info['prog'])
@click.option('-p', '--proxies', help='the proxies url, eg. http://127.0.0.1:1080', envvar='GOOGLE_PROXIES', show_envvar=True)
@click.option('-s', '--source', help='the source language', default='auto', show_default=True)
@click.option('-t', '--target', help='the target language', default='zh-CN', show_default=True)
@click.option('-l', '--languages', help='list all available languages', is_flag=True)
@click.option('-o', '--outfile', help='the output filename [stdout]')
def cli(**kwargs):


    if kwargs['languages']:
        rich.print_json(json.dumps(
            deep_translator.constants.GOOGLE_LANGUAGES_TO_CODES))
        exit(0)

    proxies = kwargs['proxies'] or os.getenv('GOOGLE_PROXIES')
    translator = Translator(source=kwargs['source'], target=kwargs['target'], proxies=proxies)
    if proxies:
        if not translator.check_proxies():
            click.secho(f'bad proxies: {proxies}', err=True, fg='red')
            exit(1)
        else:
            click.secho(f'>>> use proxies: {proxies}', err=True, fg='green')

    outfile = (kwargs['outfile'])
    out = util.safe_open(outfile, 'w') if outfile else sys.stdout
    with out:
        text = kwargs['text']
        if os.path.isfile(text):
            text = open(text).read()

        res = translator.translate(text)
        if res:
            out.write(res + '\n')
            if outfile:
                click.secho(f'safe file: {outfile}', fg='green', err=True)


def main():
    cli()


if __name__ == '__main__':
    main()
