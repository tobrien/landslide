# -*- coding: utf-8 -*-

#  Copyright 2010 Adam Zapletal
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import os


def get_abs_path_url(path):
    """ Returns the absolute url for a given local path.
    """
    return "file://%s" % os.path.abspath(path)


def get_path_url(abs_path, relative=False):
    """ Returns an absolute or relative path url from an absolute path.
    """
    if relative:
        return get_rel_path_url(abs_path)
    else:
        return get_abs_path_url(abs_path)


def get_rel_path_url(path, base_path=os.environ.get('PWD')):
    """ Returns a relative path from the absolute one passed as argument.
        Silently returns originally provided path on failure.
    """
    try:
        path_url = path.split(base_path)[1]
        if path_url.startswith('/'):
            return path_url[1:]
        else:
            return path_url
    except (IndexError, TypeError):
        return path
