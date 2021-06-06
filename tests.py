import os
from pprint import pprint

import pytest
import requests

from services import GoDaddyService, IFConfigService
from urls import GoDaddyUrls, IFCONFIG_HOST

TEST_DOMAIN = os.environ["TEST_DOMAIN"]
TEST_API_KEY = os.environ["TEST_API_KEY"]
TEST_API_SECRET = os.environ["TEST_API_SECRET"]

go_daddy_service = GoDaddyService(TEST_API_KEY, TEST_API_SECRET)
ifconfig_service = IFConfigService()


def test_get_my_dns_records():
    go_daddy_service.get_current_domain_ip(TEST_DOMAIN)


def test_get_my_ip():
    ifconfig_service.get_my_ip()


def test_set_domain_ip():
    go_daddy_service.set_domain_ip(TEST_DOMAIN, "192.168.0.5")

