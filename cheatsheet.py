#!/usr/bin/env python
# encoding: utf-8

#desc: use for key word to search the shortcut
import os.path
import glob
import sys
import yaml

COLOR_NONE = "\033[m"
COLOR_GREEN = "\033[01;32m"
COLOR_RED = "\033[01;31m"
COLOR_YELLOW = "\033[01;33m"


def get_color_str(color, msg):
    return color + msg + COLOR_NONE

def build_map(meta_map, key_map, dir_path):
    """read yaml config file to map"""
    kv_paths = glob.glob(os.path.join(dir_path, '*.kv'))
    for kv_path in kv_paths:
        filename = os.path.basename(kv_path)
        filename = filename.split('.')[0]

        f = open(kv_path)
        data = yaml.load(f)

        for key, value in data.items():
            meta_key = '[%s] %s' %(filename, key)
            meta_map.update({meta_key: value})

            if key in key_map:
                key_map.get(key).append(meta_key)
            else:
                key_map.update({key: [meta_key]})


if __name__ == '__main__':
    meta_map = {}
    key_map = {}

    path = os.path.dirname(os.path.abspath(__file__))
    dir_path = os.path.join(path, 'CSData')

    build_map(meta_map, key_map, dir_path)

    key = sys.argv[1]
    key = key.lower()
    if key in key_map:
        meta_keys = key_map.get(key)
        for meta_key in meta_keys:
            print get_color_str(COLOR_GREEN, meta_key)
            print meta_map.get(meta_key),
            print
    else:
        print get_color_str(COLOR_RED, 'miss match')





