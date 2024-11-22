from telethon import TelegramClient, events
import asyncio

api_id =
api_hash =

session_name = 'autofill_test'

client = TelegramClient(session_name, api_id, api_hash)

async def main():
    await client.start()
    print('connected')

    dialogs = await client.get_dialogs()
    for dialog in dialogs:
        print(f"Chat: {dialog.name}, ID: {dialog.id}")

    chat = await client.get_entity('Eva Kvindt')
    messages = await client.get_messages(chat, limit=1000)
    print(messages)

    chat_dict = {}
    for message in messages:
        words = message.text.split()
        for word in words:
            if word in chat_dict:
                chat_dict[word] += 1
            else:
                chat_dict[word] = 1

    print(chat_dict)

with client:
    client.loop.run_until_complete(main())