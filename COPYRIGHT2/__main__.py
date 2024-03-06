import asyncio
import importlib
from pyrogram import idle
from COPYRIGHT2 import COPYRIGHT2
from COPYRIGHT2.modules import ALL_MODULES

LOGGER_ID = -1002068936029

loop = asyncio.get_event_loop()

async def annayanx_boot():
    for all_module in ALL_MODULES:
        importlib.import_module("COPYRIGHT2.modules." + all_module)
    print("𝐁𝐎𝐓 𝐒𝐓𝐀𝐑𝐓𝐄𝐃")
    await idle()
    print("@𝐀𝐧𝐧𝐚𝐲𝐚𝐧𝐗 𝐃𝐨𝐧𝐞")
    await COPYRIGHT2.send_message(LOGGER_ID, "**˜”*°•.˜”*°• BOT DEPLOYED •°*”˜.•°*”˜ \n 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿 @𝗔𝗻𝗻𝗮𝘆𝗮𝗻𝗫 **")

if __name__ == "__main__":
    loop.run_until_complete(annayanx_boot())
    
