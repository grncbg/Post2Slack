# coding: utf-8
""" botからの送信 """

import sys
from slacker import Slacker
import slackbot_settings

ARGVS = sys.argv
ARGC = len(ARGVS)

if ARGC < 3:
    print("too few arguments")
    sys.exit()

CHANNEL = ARGVS[1]
MESSAGE = ARGVS[2]

USERNAME = "金 正恩"
ICON_EMOJI = ":kimjongun:"

if ARGC == 5:
    USERNAME = ARGVS[3]
    ICON_EMOJI = ":" + ARGVS[4] + ":"

SLACK = Slacker(slackbot_settings.API_TOKEN)
SLACK.chat.post_message(
    CHANNEL,
    MESSAGE,
    username=USERNAME,
    icon_emoji=ICON_EMOJI,
    link_names=True
    )
