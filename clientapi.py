from telethon import TelegramClient, events
from telethon.tl.functions.channels import JoinChannelRequest

api_id = 000
api_hash = ""

client = TelegramClient("session_name", api_id, api_hash)

# Event-Handler außerhalb von main()
@client.on(events.NewMessage(chats="NationForex"))
async def handler(event):
    print("Neues Signal:", event.message.text)

async def main():
    await client.start()
    await client(JoinChannelRequest("NationForex"))
    print("Bot lauuft – wartet auf neue Signale...")

# Hier NICHT client.loop.run_until_complete!
client.start()
client.loop.create_task(main())
client.run_until_disconnected()
