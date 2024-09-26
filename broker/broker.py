import logging
import os
from redis import redis
import requests
import time

DEBUG = os.environ.get("DEBUG", "").lower().startswith("y")

log = logging.getLogger(__name__)
if DEBUG:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)
    logging.getLogger("requests").setLevel(logging.WARNING)

redis = Redis("redis")

def getrngetf():
    ret = requests.get("http://rngetf/", val=val)
    return ret.content

def getrngtech():
    ret = requests.get("http://rngtech/", val=val)
    return ret.content

def getrngcrypto():
    ret = requests.get("http://rngcrypto/", val=val)
    return ret.content

def loop(int = 1):
    term = 0
    while True:
        if time.time() > term:
            log.info("Session running for {} loops")
            term = time.time() + int

def solo():
    log.debug("Solo run commencing")
    time.sleep(0.1)
    etf = getrngetf()
    tech = getrngtech()
    crypto = getrngcrypto()
    log.info("Price updated for all stocks")
    updates = redis.hset(etf, tech, crypto)


if __name__ == "__main__":
    while True:
        try:
            loop()
        except:
            log.exception("In Loop Already:")
            log.error("Attempting to reboot")
            time.sleep(5)
