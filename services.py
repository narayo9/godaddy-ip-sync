import requests

from urls import GoDaddyUrls, IFCONFIG_HOST


class GoDaddyService:
    def __init__(self, api_key: str, api_secret: str):
        self.api_key = api_key
        self.api_secret = api_secret

    @property
    def _authorization_headers(self):
        return {"Authorization": f"sso-key {self.api_key}:{self.api_secret}"}

    def get_current_domain_ip(self, domain: str):
        res = requests.get(
            GoDaddyUrls.DOMAIN_DNS_RECORD.format(domain=domain, type="A", name="@"),
            headers=self._authorization_headers,
        )
        res.raise_for_status()
        return res.json()[0]["data"]

    def set_domain_ip(self, domain: str, ip: str):
        res = requests.put(
            GoDaddyUrls.DOMAIN_DNS_RECORD.format(domain=domain, type="A", name="@"),
            headers=self._authorization_headers,
            json=[
                {
                    "data": ip,
                }
            ],
        )
        res.raise_for_status()


class IFConfigService:
    def get_my_ip(self):
        res = requests.get(IFCONFIG_HOST)
        res.raise_for_status()
        return res.text
