from telethon import TelegramClient

api_id = 32300826
api_hash = "24545744578321d45950ee2dcddaa598"

client = TelegramClient("session_name", api_id, api_hash)

async def main():
    # Telefonnummer direkt übergeben
    await client.start(phone="+4915757480630")  # deine Nummer mit +49 für Deutschland

    channel = await client.get_entity("@GoldSignalsChannel")
    async for message in client.iter_messages(channel, limit=5):
        print(message.text)

with client:
    client.loop.run_until_complete(main())
