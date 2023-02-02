from pathlib import Path


def safe_open(filename, mode='r'):
    file = Path(filename)

    if 'w' in mode and not file.parent.exists():
        file.parent.mkdir(parents=True)

    if filename.endswith('.gz'):
        import gzip
        return gzip.open(filename, mode=mode)

    return file.open(mode=mode)
