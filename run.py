import logging
import time
import argparse

from python_discord_logger import get_discord_logger

from services import GoDaddyService, IFConfigService

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--godaddy-api-key", "--key", help="Input your godaddy api key.", required=True
    )
    parser.add_argument(
        "--godaddy-api-secret",
        "--secret",
        help="Input your godaddy api secret.",
        required=True,
    )
    parser.add_argument(
        "--domain", "-D", help="Input your domain to sync.", required=True
    )

    parser.add_argument(
        "--interval",
        "-I",
        help="Time interval minutes to check and set.",
        type=int,
        default=60,
    )
    parser.add_argument("--webhook-url", "-U", help="Webhook url to log.")
    parser.add_argument("--webhook-user-id", help="Webhook user id to be tagged.")
    parser.add_argument("--loglevel", help="Set logger level", default="DEBUG")

    args = parser.parse_args()

    godaddy_service = GoDaddyService(args.godaddy_api_key, args.godaddy_api_secret)
    ifconfig_service = IFConfigService()
    webhook_url = args.webhook_url
    webhook_user_id = args.webhook_user_id
    domain = args.domain
    interval = args.interval

    if webhook_url:
        logger = get_discord_logger(__name__, webhook_url, webhook_user_id)
    else:
        logger = logging.getLogger(__name__)

    logger.addHandler(logging.StreamHandler())
    logger.setLevel(args.loglevel)
    while True:
        try:
            logger.info(f"**IP Sync on domain: {domain}** Start")
            current_ip = godaddy_service.get_current_domain_ip(domain)
            my_ip = ifconfig_service.get_my_ip()

            if current_ip != my_ip:
                godaddy_service.set_domain_ip(domain, my_ip)
            logger.info(f"**IP Sync on domain: {domain}** Success")
        except Exception as e:
            logger.error(f"**IP Sync on domain: {domain}** Error", exc_info=e)

        logger.info(f"**IP Sync on domain: {domain}** Start sleeping for {interval} minutes.")
        time.sleep(interval * 60)
