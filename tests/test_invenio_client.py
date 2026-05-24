# SPDX-FileCopyrightText: 2024 CERN.
# SPDX-License-Identifier: MIT

"""Module tests."""

# from inveniordm_py import InvenioAPI


# def test_client(token, base_url, mocked_session):
#     client = InvenioAPI(base_url, token, session=mocked_session)

#     res = client.records.search()

#     for r in res:
#         r.versions

#     client.records.create()
#     # client.records("1234").files.download() # TODO uncomment when files are implemented

#     r = client.records("1234").get()

#     assert r.data is not None
#     assert r.versions.latest() is not None
