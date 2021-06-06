GO_DADDY_HOST = "https://api.godaddy.com"


class GoDaddyUrls:
    DOMAIN = f"{GO_DADDY_HOST}/v1/domains/{{domain}}"
    DOMAIN_DNS_RECORD = (
        f"{GO_DADDY_HOST}/v1/domains/{{domain}}/records/{{type}}/{{name}}"
    )


IFCONFIG_HOST = "https://ifconfig.me"
