import os
import json
import pytest
from urllib import parse


@pytest.fixture("module")
def vcr_config():
    return dict(
        record_mode=os.environ.get("VCR") or "once",  # Set to NONE in travis
        decode_compressed_response=True,
        serializer="yaml",
        filter_post_data_parameters=[
            ("client_id", "HIDDEN"),
            ("client_secret", "HIDDEN"),
            (os.environ.get("CLIENT_ID"), "HIDDEN"),
            (os.environ.get("CLIENT_SECRET"), "HIDDEN"),
            (os.environ.get("USER_ID"), "HIDDEN"),
        ],
        filter_headers=[
            ("Authorization", "HIDDEN"),
            (os.environ.get("CLIENT_ID"), "HIDDEN"),
            (os.environ.get("CLIENT_SECRET"), "HIDDEN"),
            (os.environ.get("USER_ID"), "HIDDEN"),
        ],
        cassette_library_dir="tests/vcr_cassettes/",
        before_record_request=vcr_custom_request_filter,
        before_record_response=vcr_custom_response_filter,
    )


def vcr_custom_request_filter(request):
    hidden_values = [(os.environ.get("CLIENT_ID")), (os.environ.get("CLIENT_SECRET")), (os.environ.get("USER_ID"))]
    new_url, _ = parse.splitquery(request.uri)

    for value in hidden_values:
        new_url = new_url.replace(value, "HIDDEN")

    request.uri = new_url
    return request


def vcr_custom_response_filter(response):
    values_to_hide = [
        os.environ.get("CLIENT_ID"),
        os.environ.get("CLIENT_SECRET"),
        os.environ.get("USER_ID"),
        "access_token",
        "user_id",
        "refresh_token",
        "id",
        "nickname",
        "last_name",
        "email",
        "identification",
        "address",
        "phone",
        "alternative_phone",
        "permalink",
        "secure_email",
        "street_name",
        "address_line",
        "street_number",
        "city",
        "state",
        "latitude",
        "longitude",
        "address_line",
        "name",
        "owner_id",
        "short_name",
        "url",
        "test_access_token",
    ]

    string = response["body"]["string"].decode()
    body = json.loads(string)
    new_list = []
    if isinstance(body, list):
        for new_dict in body:
            new_list.append(hide_values(new_dict, values_to_hide))
        body = new_list
    else:
        body = hide_values(body, values_to_hide)

    if "address" in body:
        body["address"] = {"address": "some address", "city": "some city", "state": "some state", "zip_code": "1234"}
    if "phone" in body:
        body["phone"] = {"area_code": "area", "extension": "extension", "number": "number", "verified": False}

    response["body"]["string"] = json.dumps(body).encode()
    return response


def hide_values(source, values_to_hide):
    for key in values_to_hide:
        if key in source:
            source[key] = "HIDDEN"
    return source
