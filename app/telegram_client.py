import asyncio
import time

from telethon import TelegramClient
from telethon.errors import PeerFloodError
from telethon.tl.functions.contacts import ImportContactsRequest
from telethon.tl.types import InputPhoneContact

from app.config import settings


def send_to_telegram(phone: str, message: str, qr_code_link: str, full_name: []):
    session = settings.TELEGRAM_USERNAME
    api_id = settings.TG_API_ID
    api_hash = settings.TG_API_HASH
    telegram_phone_number = settings.TELEGRAM_PHONE_NUMBER
    password_tg = settings.TELEGRAM_PASSWORD

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    client = TelegramClient(session, api_id, api_hash,
                            sequential_updates=True).start(telegram_phone_number, password_tg)

    async def main(phone1: str):
        contact = InputPhoneContact(
            client_id=0,
            phone=phone1,
            first_name=full_name[0],
            last_name=full_name[1]
        )
        await client(ImportContactsRequest([contact]))

        try:
            user = await client.get_entity(phone1)
            await client.send_file(user, qr_code_link, caption=message)
            time.sleep(61)
            return 'Отправлено в телеграм'
        except (Exception, PeerFloodError) as e:
            # if e == 'Too many requests (caused by SendMediaRequest)':
            #     time.sleep(61)
            #     user = await client.get_entity(phone1)
            #     await client.send_file(user, qr_code_link, caption=message)
            return e

    with client:
        client.loop.run_until_complete(main(phone))
