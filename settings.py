# Maximum request times, follow the limit update from Binance to avoid being banned
COUNT_REQUESTS = 150

# Give it here - https://2captcha.com/enterpage
CAPTCHA_API_KEY = ''

# Yours own proxy here `username:password@ip:port` [NOT REQUIRED]
PROXY = ''

# Login info, check your Fetch/XHR -> auth
BNC_UUID = ''
COOKIE = ''
CSRFTOKEN = ''
DEVICE_INFO = ''
USER_AGENT = ''

# Don't touch atm
BINANCE_SITEKEY = '6LeUPckbAAAAAIX0YxfqgiXvD3EOXSeuq0OpO8u_'

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
