# (c) Asm Safone
# A Part of MegaDL-Bot <https://github.com/AsmSafone/MegaDL-Bot>


import os

class Config:
    API_ID = int(os.environ.get("API_ID", 123))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    TG_MAX_SIZE = 2040108421
    OWNER_ID = int(os.environ.get("OWNER_ID", 828779943))
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)


class TEXT:
  ABOUT = """
๐ค **Nume:** {bot_name}

๐ **Am fost programat in:** [Python](https://www.python.org)

๐ **Library:** [Pyrogram](https://docs.pyrogram.org)

๐ก **Sunt Hostat pe:** [Heroku](https://heroku.com)

๐งโ๐ป **Developer:** [Iarbadevanzare](https://t.me/iarbadevanzare)

๐ฅ **Grup Support:** [๐ฆ๐ฑ ๐ดโโ ๏ธ ๐๐ฃ๐ก แดาาษชแดษชแดส ๐ดโโ ๏ธ ๐ฆ๐ฑ ๐น๐ฉ](https://t.me/otrofficial)

๐ข **Canalele noastre si boti:** [๐ท๐ด Portal โ OTR ๐ฆ๐ฑ](https://t.me/OTRportal)
"""

  HELP_USER = """
Eu sunt **{bot_name}**\n\nAcest bot poate descarca fisiere & video de pe linkurile Mega si sa le incarce pe Telegram.\nDoar trimite un link Mega.nz (nu folder) si asteapta sa vezi magia๐ฎ\n\n**Poti oricand sa adaugi sau sa modifici un text:** doar alege un tip de fisier sau video deja trimis de mine dupa care poti face forward la un **telegraph cu textul dorit** ca raspuns la acesta si el va aparea sub video ๐!\n**Made With ๐ช๐ป By @OTRportal! ๐ฅ**
"""

  START_TEXT = """
๐๐ป **Salut/Buna** {user_mention},\n\nEu sunt **{bot_name}**\n**Pot descarca fisiere & video de pe Mega.nz** & le pot incarca la tine pe Telegram.\n**Te rog sa apesi pe AJUTOR** pentru a putea afla mai multe ๐!\n\n**BOT Owner: {bot_owner}**๐!
"""
