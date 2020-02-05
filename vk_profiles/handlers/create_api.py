import logging

import vk_requests

from vk_profiles.handlers.LogStream import LogStream


def create_api(login, password):
    log_stream = LogStream()
    # Setup basic config
    logging.basicConfig(
        stream=log_stream,
        level=logging.INFO,
        format='%(asctime)s %(levelname)s [%(name)s] %(message)s',
    )
    # To change log level for the library logger
    logging.getLogger('vk-requests').setLevel(logging.DEBUG)
    api = vk_requests.create_api(app_id=7306186, login=login, password=password)
    return api, log_stream
