# coding: utf-8
""" botからの送信 """

from slacker import Slacker
import slackbot_settings

CHANNEL = "bot-test"
MESSAGE = "message"
USERNAME = "user"
ICON_EMOJI = ":smile:"
AS_USER = False

SLACK = Slacker(slackbot_settings.API_TOKEN)
SLACK.chat.post_message(
    CHANNEL,
    MESSAGE,
    username=USERNAME,
    icon_emoji=ICON_EMOJI,
    as_user=AS_USER,
    link_names=True
    )
