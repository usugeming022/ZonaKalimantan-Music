# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith 

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.




from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"𝘏𝘢𝘭𝘰 𝙆𝙖𝙢𝙪!, ** 𝘚𝘢𝘺𝘢 𝘈𝘥𝘢𝘭𝘢𝘩 𝘓𝘢𝘺𝘢𝘯𝘢𝘯 ⚡️𝙈𝙪𝙨𝙞𝙠-𝙆𝙞𝙣𝙜⚡️.**\n\n ❗️ 𝙍𝙪𝙡𝙚𝙨:\n   - Jika bot terjadi masalah , silahkan pm ( chat ) @PacarFerdilla\n   - Jangan spam Lagu biar ga error ya \n\n 👉 **KIRIM LINK UNDANGAN GRUP ATAU NAMA PENGGUNA JIKA USERBOT TIDAK DAPAT BERGABUNG DENGAN GRUP ANDA.**\n\n ⛑ **Grup Support :** @KingUserbotSupport - **Master** @mPacarFerdilla\n\n")
  return                        