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
    cmd = 'jslint --terse --'
    regex = r'^.+?:(?P<line>\d+):(?P<col>\d+): (?P<message>.+)$'
    tempfile_suffix = {
        'javascript': 'js',
        'html': 'html'
    }
    error_stream = util.STREAM_STDOUT
    selectors = {
        'html': 'source.js.embedded.html'
    }
    word_re = None
    comment_re = r'\s*/[/*]'
