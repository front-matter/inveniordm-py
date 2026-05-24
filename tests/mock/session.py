# SPDX-FileCopyrightText: 2024 CERN.
# SPDX-License-Identifier: MIT
"""Mock session."""

from unittest.mock import MagicMock

from .request import MockRequest
from .response import MockResponse


class MockSession(MagicMock):
    """Mock session."""

    def post(self, *args, **kwargs):
        """Mock post method."""
        req = MockRequest(
            data=kwargs.get("data"),
            headers=kwargs.get("headers"),
            url=args[0],
            method="POST",
        )
        return MockResponse(request=req)

    def put(self, *args, **kwargs):
        """Mock put method."""
        req = MockRequest(
            data=kwargs.get("data"),
            headers=kwargs.get("headers"),
            url=args[0],
            method="PUT",
        )
        return MockResponse(request=req)

    def get(self, *args, **kwargs):
        """Mock get method."""
        req = MockRequest(
            data=kwargs.get("data"),
            headers=kwargs.get("headers"),
            url=args[0],
            method="GET",
        )
        return MockResponse(request=req)
