from telethon import TelegramClient, events

api_id = 32300826
api_hash = "24545744578321d45950ee2dcddaa598"

client = TelegramClient("session_name", api_id, api_hash)

@client.on(events.NewMessage(chats=1486169736))  # deine Kanal-ID
async def handler(event):
    print("[Gold Signals] Neues Signal:", event.message.text)

async def main():
    await client.start()
    print("Bot läuft – wartet auf neue Nachrichten...")
    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())
