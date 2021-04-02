"""Notlar için Pyrogram Akıllı Eklentisi t.me/VCSets

Required chat permission:
- Delete messages
"""
from pyrogram import Client, filters, emoji
from pyrogram.types import Message

notes = {}
url = {}
response = {}

notes['notes'] = f"""{emoji.SPIRAL_NOTEPAD} **Notlar** (/notes):

`#notes` __list all notes__
`#heroku` __deploy to heroku__
`#raw` __raw pcm file size__
`#repo` __repository__
`#musicbot` __tgmusicbot__"""

url['readme_heroku'] = (
    "https://github.com/callsmusic/tgvc-userbot#deploy-to-heroku"
)
url['heroku'] = (
    "https://heroku.com/deploy?template="
    "https://github.com/callsmusic/tgvc-userbot/tree/dev"
)
url['replit'] = "https://repl.it/@Leorio/stringsessiongen#main.py"
notes['heroku'] = f"""{emoji.LABEL} **Heroku** (/notes #heroku):

{emoji.BACKHAND_INDEX_POINTING_RIGHT} [Deploy to Heroku]({url['heroku']})
{emoji.SPIRAL_NOTEPAD} [README]({url['readme_heroku']})


**Session String**:
__choose one of the two__

- Run [the code]({url['readme_heroku']}) tek başına
- [replit]({url['replit']}), kendi riskinizle kullanmak"""

notes['raw'] = f"""{emoji.LABEL} **RAW PCM dosya boyutu** (/notes #raw):

`filesize_in_bytes / second == channel * sample_rate * bit_depth / 8`

```| duration | filesize |
|----------|----------|
|       1M |   10.98M |
|       4M |   43.94M |
|      10M |  109.86M |
|       1H |  659.17M |
|       2H |    1.28G |
|       4H |    2.57G |```"""

url['repo'] = "https://github.com/callsmusic/tgvc-userbot"
notes['repo'] = f"""{emoji.LABEL} **Repository** (/notes #repo):

{emoji.ROBOT} [Telegram Voice Chat Userbot (tgvc-userbot)]({url['repo']})"""

url['tmbh'] = (
    "https://heroku.com/deploy?template="
    "https://github.com/callsmusic/tgmusicbot"
)
notes['musicbot'] = (
    f"""{emoji.ROBOT} **Telegram Music Bot** (/notes #musicbot):
__bot for downloading music from YouTube/SoundCloud/Mixcloud__

**Repository**: [GitHub](https://github.com/callsmusic/tgmusicbot)
**License**: AGPL-3.0-or-later

{emoji.BACKHAND_INDEX_POINTING_RIGHT} [Deploy to Heroku]({url['tmbh']})"""
)


@Client.on_message(
    filters.chat("VCSets")
    & filters.text
    & ~filters.edited
    & (filters.command(list(notes.keys()), prefixes="#")
       | filters.command("notes", prefixes="/"))
)
async def show_notes(_, m: Message):
    if len(m.command) != 1:
        return
    m_target, quote = (m.reply_to_message or m), bool(m.reply_to_message)
    m_response = await m_target.reply_text(
        notes[m.command[0]],
        quote=quote,
        disable_web_page_preview=True
    )
    await m.delete()
    key = 'list' if m.command[0] == 'notes' else 'note'
    if response.get(key) is not None:
        await response[key].delete()
    response[key] = m_response
