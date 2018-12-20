import json
import pytest
from urllib import parse


@pytest.fixture(scope="module")
def vcr_config():
    return dict(
            record_mode='once',  # Set to NONE in travis
            decode_compressed_response=True,
            filter_post_data_parameters=[
                ('client_id', 'HIDDEN'),
                ('client_secret', 'HIDDEN'),
            ],
            filter_headers=[
                ('Authorization', 'HIDDEN'),
            ],
            cassette_library_dir='tests/vcr_cassettes/',
            before_record_request=vcr_custom_request_filter,
            before_record_response=vcr_custom_response_filter,
            )


def vcr_custom_request_filter(request):
    request.uri, _ = parse.splitquery(request.uri)
    return request


def vcr_custom_response_filter(response):
    values_to_hide = [
        'access_token',
        'user_id',
        'refresh_token',
        'id',
        'nickname',
        'last_name',
        'email',
        'identification',
        'address',
        'phone',
        'alternative_phone',
        'permalink',
        'secure_email',
        'street_name',
        'address_line',
        'street_number',
        'city',
        'state',
        'latitude',
        'longitude',
        'address_line',
        'name',
        'owner_id',
        'short_name',
        'url',
        'test_access_token',


    ]
    string = response['body']['string'].decode('utf-8')
    body = json.loads(string)
    new_list = []
    if isinstance(body, list):
        for new_dict in body:
            new_list.append(hide_values(new_dict, values_to_hide))
        body = new_list
    else:
        body = hide_values(body, values_to_hide)

    response['body']['string'] = json.dumps(body).encode()
    return response


def hide_values(source, values_to_hide):
    for key in values_to_hide:
        if key in source:
            source[key] = 'HIDDEN'
    return source
