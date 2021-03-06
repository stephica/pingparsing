# encoding: utf-8

"""
.. codeauthor:: Tsuyoshi Hombashi <tsuyoshi.hombashi@gmail.com>
"""

from __future__ import absolute_import


class PingStaticticsHeaderNotFoundError(Exception):
    """
    Exception raised when a ping statistics header not found in
    a parsing text.
    """


class EmptyPingStaticticsError(Exception):
    """
    Exception raised when a ping statistics is empty in a parsing text.
    """
