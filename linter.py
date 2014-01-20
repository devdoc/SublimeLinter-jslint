#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Rasmus Paetau
# Copyright (c) 2014 Rasmus Paetau
#
# License: MIT
#

"""This module exports the Jslint plugin class."""

from SublimeLinter.lint import Linter, util


class Jslint(Linter):

    """Provides an interface to jslint."""

    syntax = ('javascript', 'html')
    cmd = 'jslint'
    executable = 'jslint'
    regex = r'^\s*#\d+ (?P<message>.+)\n\s{4}.*// Line (?P<line>\d+), Pos (?P<col>\d+)$'
    multiline = True
    line_col_base = (1, 1)
    tempfile_suffix = "tmp"
    error_stream = util.STREAM_STDOUT
    selectors = {
        'html': 'source.js.embedded.html'
    }
    word_re = None
    defaults = {}
    inline_settings = None
    inline_overrides = None
    comment_re = r'\s*/[/*]'
