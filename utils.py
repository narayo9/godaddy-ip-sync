import requests


def get_authorization_headers(api_key: str, api_secret: str):
    return {
        'Authorization': f'sso-key {api_key}:{api_secret}'
    }