import discord
import os


client = discord.Client()


@client.event
async def on_ready():
    print("로그인")
    print(client.user.name)
    print(client.user.id)
    print("------------------")
    await client.change_presence(game=discord.Game(name='삼창청소중', type=1))


@client.event
async def on_message(message):
    if message.content.startswith("!인사"):
        await client.send_message(message.channel, "삼창에 오신걸 환영합니다")
    if message.content.startswith("!고니"):
        await client.send_message(message.channel, "고니는 멍청해")
    if message.content.startswith("!삼창"):
        await client.send_message(message.channel, "삼창에 내리세요!!!!")
    if message.content.startswith("!맞짱"):
        await client.send_message(message.channel, "확실한건 고니는 처맞아요")
    if message.content.startswith("!부캠"):
        await client.send_message(message.channel, "와이자 세팀!!")
    if message.content.startswith("!파밍"):
        await client.send_message(message.channel, "드링크 하나만 주세요")
        
        
access_token = os.environ["BOT_TOKEN"]        
client.run(access_token)
