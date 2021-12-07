COUNT_REQUESTS = 150

# Give it here - https://2captcha.com/enterpage
CAPTCHA_API_KEY = ''

BINANCE_SITEKEY = '6LeUPckbAAAAAIX0YxfqgiXvD3EOXSeuq0OpO8u_'

# Yours own proxy here `username:password@ip:port` [NOT REQUIRE]
PROXY = ''

CSRFTOKEN = ''
COOKIE = ''

USER_AGENT = ''
DEVICE_INFO = ''
BNC_UUID = ''

headers = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9,ru;q=0.8",
    "bnc-uuid": BNC_UUID,
    "clienttype": "web",
    "content-type": "application/json",
    "cookie": COOKIE.encode("UTF-8"),
    "csrftoken": CSRFTOKEN,
    "device-info": DEVICE_INFO,
    "user-agent": USER_AGENT,
    "lang": "en",
    "x-nft-checkbot-sitekey": BINANCE_SITEKEY,
}
