# This is an alternate version of python written by DrogazDevelopent for discord developers to easy things up with export data to an discord server. © Drogaz Developent 2022 - DO NOT ADD OR REMOVE THINGS IN THIS FILE!

from discord_webhook import DiscordWebhook, DiscordEmbed


def defaultMessage(Webhook, Content):
    webhook = DiscordWebhook(url=Webhook,
                             content=Content,
                             username="pyDrogaz", avatar_url="https://avatars.githubusercontent.com/u/36101493?s=200&v=4")
    response = webhook.execute()
    print("Message sent")


def embedMessage(Webhook, Title, Desc, ColorInHex, EmbedName, amount):
    webhook = DiscordWebhook(url=Webhook, username="pyDrogaz", avatar_url="https://avatars.githubusercontent.com/u/36101493?s=200&v=4")
    EmbedName = DiscordEmbed(title=Title, description=Desc, color=ColorInHex)
    x = 0
    while x < amount:
      EmbedName.add_embed_field(name='Field 1', value='Lorem ipsum')
      x = x + 1
    webhook.add_embed(EmbedName)
    response = webhook.execute()
    print("Default Embed sent")


def sendFile(Webhook, File):
    webhook = DiscordWebhook(url=Webhook, username="pyDrogaz", avatar_url="https://avatars.githubusercontent.com/u/36101493?s=200&v=4")
    with open(File, "rb") as f:
        webhook.add_file(file=f.read(), filename=File)

    response = webhook.execute()


#test.add_embed_field(name='Field 1', value='Lorem ipsum')
