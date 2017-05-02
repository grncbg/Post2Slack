# coding: utf-8
""" botからの送信 """

from slacker import Slacker
import slackbot_settings

SLACK = Slacker(slackbot_settings.API_TOKEN)
SLACK.chat.post_message(
    "channel",
    "message",
    username="username",
    icon_emoji=":emoji:",
    link_names=True
    )
