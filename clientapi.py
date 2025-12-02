from telethon import TelegramClient, events
from telethon.tl.functions.channels import JoinChannelRequest

api_id = 32300826
api_hash = "24545744578321d45950ee2dcddaa598"

client = TelegramClient("session_name", api_id, api_hash)

async def main():
    # Startet den Client (fragt dich beim ersten Mal nach dem Login-Code)
    await client.start()

    # Kanal beitreten (falls noch nicht Mitglied)
    await client(JoinChannelRequest("@UnitedSignals"))

    print("Bot laeuft  wartet auf neue Signale...")

    # Event-Handler für neue Nachrichten im Kanal
    @client.on(events.NewMessage(chats="@UnitedSignals"))
   # @client.on(events.NewMessage(chats="@UnitedSignals"))
    #channel = await client.get_entity("@BBC_News0")


    async def handler(event):
        print("Neues Signal:", event.message.text)

    # Client dauerhaft laufen lassen
    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())
