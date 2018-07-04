# -*- coding: utf-8 -*-
"""Utils tasks for files operations and settings operations"""


import json
from os import path
from sys import version_info


def path_format(file_path=None, file_name=None, is_abspath=False,
                ignore_raises=False):
    """
    Get path joined checking before if path and filepath exist,
     if not, raise an Exception
     if ignore_raise it's enabled, then file_path must include '/' at end lane
    """
    path_formatted = "{}{}".format(file_path, file_name)
    if ignore_raises:
        return path_formatted
    if file_path is None or not path.exists(file_path):
        raise IOError("Path '{}' doesn't exists".format(file_path))
    if file_name is None or not path.exists(path_formatted):
        raise IOError(
            "File '{}{}' doesn't exists".format(file_path, file_name))
    if is_abspath:
        return path.abspath(path.join(file_path, file_name))
    else:
        return path.join(file_path, file_name)


def read_file(is_json=False, file_path=None, encoding='utf-8',
              is_encoding=True):
    """Returns file object from file_path,
       compatible with all py versiones
    optionals:
      can be use to return dict from json path
      can modify encoding used to obtain file
    """
    text = None
    if file_path is None:
        raise Exception("File path received it's None")
    if version_info.major >= 3:
        if not is_encoding:
            encoding = None
        with open(file_path, encoding=encoding) as buff:
            text = buff.read()
    if version_info.major <= 2:
        with open(file_path) as buff:
            if is_encoding:
                text = buff.read().decode(encoding)
            else:
                text = buff.read()
    if is_json:
        return json.loads(text)
    return text


def settings(file_path='./', file_name='settings.json',
             is_abspath=True):
    """Returns file settings as a dict to be use on qacode lib"""
    return read_file(is_json=True,
                     file_path=path_format(file_path=file_path,
                                           file_name=file_name,
                                           is_abspath=is_abspath))