print("\n\n\n\n\nHello sir!!, I'm Here To Help u to Generate Telethon String Session")
print("\n\nXtreme UserBot")

print("\n\nProperly Fill APP_ID ,HASH and Number.\n")

from telethon.sync import TelegramClient
from telethon.sessions import StringSession
APP_ID = int(input("Enter APP ID here: "))
API_HASH = input("Enter API HASH here: ")
with TelegramClient(StringSession(), APP_ID, API_HASH) as hehe:
	dcsession = hehe.session.save()
	dcobra = hehe.send_message(
	    "me",
	    f"`{dcsession}`\n\n**Your Xtreme userbot String Session Here Sir😁😎😎\nClick on above Code to Copy it\n\nFor Support Join** @xtreme_userbot"
	)

print("\n\n############################\n")
print(
    "check your Telegram Saved Messages For Ur New String String Session 😂😂 or see below. ")

print("\n############################\n")


print(f"{dcsession}")

Print(" ")
