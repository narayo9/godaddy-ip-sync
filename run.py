import typing
import argparse

def set_a_name_to_ip(ip: str, domain: str):
    pass


def run(webhook_url: str, webhook_user_id: typing.Optional[str] = None):
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('')

    parser.add_argument("--webhook-url", "-U", help="Webhook url to log.")
    parser.add_argument("--webhook-user-id", help="Webhook user id to be tagged.")

