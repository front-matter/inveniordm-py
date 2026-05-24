# SPDX-FileCopyrightText: 2024 CERN.
# SPDX-License-Identifier: MIT

"""Pytest configuration."""

import pytest

from inveniordm_py import InvenioAPI

from .mock.session import MockSession


@pytest.fixture(scope="module")
def base_url():
    """Base URL of the REST API."""
    return "https://127.0.0.1"


@pytest.fixture(scope="module")
def token():
    """Mocked authentication token."""
    return "test"


@pytest.fixture(scope="module")
def mocked_session():
    """Mock HTTP session used by the client."""
    yield MockSession()


@pytest.fixture(scope="module")
def client(base_url, token, mocked_session):
    """Inveniordm REST API client."""
    return InvenioAPI(base_url, token, session=mocked_session)


@pytest.fixture(scope="module")
def minimal_record():
    """Minimal record metadata."""
    return {
        "access": {"record": "public", "files": "public"},
        "files": {"enabled": True},
        "metadata": {
            "creators": [
                {
                    "person_or_org": {
                        "family_name": "Brown",
                        "given_name": "Troy",
                        "type": "personal",
                    }
                },
                {
                    "person_or_org": {
                        "family_name": "Collins",
                        "given_name": "Thomas",
                        "identifiers": [
                            {"scheme": "orcid", "identifier": "0000-0002-1825-0097"}
                        ],
                        "name": "Collins, Thomas",
                        "type": "personal",
                    },
                    "affiliations": [{"id": "01ggx4157", "name": "Entity One"}],
                },
            ],
            "publication_date": "2020-06-01",
            "resource_type": {"id": "image-photo"},
            "title": "A Romans story",
        },
    }
