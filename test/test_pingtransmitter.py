"""
.. codeauthor:: Tsuyoshi Hombashi <gogogo.vm@gmail.com>
"""

from __future__ import unicode_literals

import pytest

from pingparsing import *


class Test_PingTransmitter_ping:

    @pytest.mark.parametrize(["host", "waittime", "expected"], [
        ["", 1, ValueError],
        ["test", 0, ValueError],
        ["test", -1, ValueError],
    ])
    def test_except(self, host, waittime, expected):
        transmitter = PingTransmitter()
        transmitter.destination_host = host
        transmitter.waittime = waittime
        with pytest.raises(expected):
            transmitter.ping()
