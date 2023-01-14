# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

from base64 import b64decode
from os import getenv

from dotenv import load_dotenv

load_dotenv("config.env")


API_HASH = getenv("API_HASH", "b123825921f145a0c20e96848508c07b")
API_ID = int(getenv("API_ID", "18735309"))
BLACKLIST_CHAT = getenv("BLACKLIST_CHAT", None)
if not BLACKLIST_CHAT:
    BLACKLIST_CHAT = [-1001473548283]
BLACKLIST_GCAST = {int(x) for x in getenv("BLACKLIST_GCAST", "893699890").split()}
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID", "893699890") or 0)
BOT_VER = "0.2.0@main"
BRANCH = "main"
CHANNEL = getenv("CHANNEL", "Lunatic0de")
CMD_HANDLER = getenv("CMD_HANDLER", ".")
DB_URL = getenv("DATABASE_URL", "")
GIT_TOKEN = getenv(
    "GIT_TOKEN", "5651006984:AAHJzYCmETATB_aCRIROOhJUvPUfNsRIIEk"
    b64decode("").decode(
        "utf-8"
    ),
)
GROUP = getenv("GROUP", "SharingUserbot")
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
PMPERMIT_PIC = getenv("PMPERMIT_PIC", None)
REPO_URL = getenv(
    "REPO_URL", "https://github.com/mrismanaziz/PyroMan-Userbot"
    b64decode("aHR0cHM6Ly9naXRodWIuY29tL3Byb2plY3RtNG4vUHlyb01hbg==").decode("utf-8"),
)
STRING_SESSION1 = getenv("STRING_SESSION1", "1BVtsOKEBuxVh9UFkRQNLZuJLSqeqybhP2WZSF2q6Iq8NJ-JaBVGUCgO4LbZ_0cR-MZ96-OQ36On-z1Z0Mv0p-eBw1gmaoZxfGF6gOoVJxquTagjZX24B7X8damHdCr0pXdr9rFICkcEUcSSKDNigN5Lnh-1hSXyAfdWcIYG2s7YOsM1wC8xV3Ddb0ZlZB0-BEwxdqcDbKTn0hlewMFh7kh6brDWqcXPOMDNsGMQ98lMRpak_dn9Rd9dLMe-v7RHNw-uecSZRWZodtcpH13LuvCJW0KjRY8ubZ3piqRn4Pd8zltkMAkmH3ins_ADOmx5VAMZvL56dpQ704SppMsknQYDW6q1OFyY=")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
