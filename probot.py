import re
import time
import discord
import asyncio
client = discord.Client()
played = discord.Game(name=".info | .help")

@client.event
async def on_ready():
    print("Logged in as :", client.user.name)
    print("ID :", client.user.id)
    print("Ready")
    await client.change_presence(game=played)
    print("Playing : ", played.name)

#@client.event
#async def on_member_join(member)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    elif message.content.startswith('.'):
        text = message.content[1:] # the message's content without the .
        endCommand = text.find(" ")+1
        contenu = str(text[endCommand:])

        if text == "help":
            content = "`.help` Affiche ce menu. ( Tu viens de le faire, non ? :thinking:)\n\
`.ping` Donne la latence du bot.\n\
`.info` Affiche la description de ProBot\n\
`.invite` Donne un lien pour inviter ProBot"
            emb = discord.Embed(description=content)
            emb.set_author(name="Probot's help menu", icon_url=client.user.avatar_url)
            await client.send_message(message.channel, embed=emb)

        if text == "ping":
            timePing = time.monotonic()
            pinger = await client.send_message(message.channel, ":ping_pong: **Pong !**")
            ping = '%.2f' % (1000*(time.monotonic()-timePing))
            await client.edit_message(pinger, ":ping_pong: **Pong !**\nLatence : " + '`' + ping + " ms`.")

        if text.startswith("say"):
            arguments = text[4:].split(" | ")
            print(arguments)
            if "^#" in arguments:
                print("un #")
            target = message.channel

            emb = discord.Embed(title="Title", description="Hope it's working...")
            #emb.set_author(name=client.user.name, icon_url=client.user.avatar_url)
            await client.send_message(target, embed=emb)

        if text == "info":
            content = "*Mince, c'est là qu'il faut se présenter...*\n\
**Hey, salut à ~~toutes~~ et à tous !** ; ici pour augmenter le nombre de membres et faire pro.\n\
Utilisez `.help` pour la liste des commandes.\n"
            emb = discord.Embed(description=content)
            emb.set_author(name="Probot, official ProTech's bot", icon_url=client.user.avatar_url)
            emb.set_footer(text="Coded with ❤ by FrenchMasterSword#5079")
            await client.send_message(message.channel, embed=emb)

        #if text == "invite":



        #if message.author.top_role >=

#def say(content, titre, couleur=0xcacbce, target=message.channel):
  #  emb = discord.Embed(description=content, colour=couleur)
    #emb.set_author(name=titre, icon_url=client.user.avatar_url)
    #await client.send_message(target, embed=emb)


client.run("NDA5MjM5MDY2NzAyMzgxMDY2.DVdB1g.s2gQ7rhrw4iAuSClM-dtGv4BMFM")
