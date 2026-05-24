# SPDX-FileCopyrightText: 2024 CERN.
# SPDX-License-Identifier: MIT
"""Mock requests module for inveniordm-py tests."""

from unittest.mock import MagicMock


class MockRequest(MagicMock):
    """Mock request object.""" ""

    def __init__(self, *args, **kwargs):
        """Constructor.

        Data and headers are passed as kwargs.
        """
        super().__init__(*args, **kwargs)
        self.headers = kwargs.get("headers") or {}
        self.data = kwargs.get("data") or {}
        self.url = kwargs.get("url") or ""
        self.method = kwargs.get("method") or ""
