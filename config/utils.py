from pathlib import Path
from datetime import datetime


def dt2f(x):
    """
    Datetime to Filetime.
    :param x:
    :return:
    """
    return x.strftime('%Y-%m-%d %H:%M:%S')


def ts2dt(x):
    """
    Timestamp to Datetime.
    :param x:
    :return:
    """
    return datetime.fromtimestamp(x)


def ts2dt2f(x):
    """
    Timestamp to Datetime to Filetime.
    :param x:
    :return:
    """
    return dt2f(ts2dt(x))


def from_args(args, key):
    """
    Lazy key from args.
    :param args:
    :param key:
    :return:
    """
    return args[key] if args.__contains__(key) else f'ERROR'


def from_args_fallback(args, key, fallback):
    """
    Lazy key from args else fallback message.
    :param args:
    :param key:
    :param fallback:
    :return:
    """
    return args[key] if args.__contains__(key) else f'{fallback}'


def from_args_fallback_int(args, key, fallback):
    """
    Lazy key from args else fallback func.
    :param args:
    :param key:
    :param fallback:
    :return:
    """
    return int(args[key]) if args.__contains__(key) else fallback


def to_decimal__xy(x, y):
    """
    Result to 2 deep float.
    :param x:
    :param y:
    :return:
    """
    return '{0:2.2f}'.format(x / y)


def to_percent__xy(x, y):
    """
    Result to 2 deep percent.
    :param x:
    :param y:
    :return:
    """
    return '{:.2%}'.format(x / y)


def to_percent(x):
    """
    Value to 2 deep percent.
    :param x:
    :return:
    """
    return '{:.2%}'.format(x)


def format_percent(x):
    """
    Add 2 deep val and % sign to percent.
    :param x:
    :return:
    """
    return '{0:2.2f}{1}'.format(x, '%')


def format_column_header(string):
    """
    Normalize column header.
    :param string:
    :return:
    """
    _name = str(string).lower()
    _name = f'{_name[0].upper()}{_name[1:]}'
    _name = _name.replace('_', ' ').replace('-', ' ')
    return _name


def create_ifnexist(path):
    """
    Lazy create if not exists.
    :param path:
    :return:
    """
    if not path.exists():
        if not Path(path.parent).exists():
            if path != path.drive:
                create_ifnexist(Path(path.parent))
        path.mkdir()
