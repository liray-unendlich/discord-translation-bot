import discord
import requests
import re
import asyncio

client = discord.Client()
url = 'https://translate.google.com/?hl=ja#en/ja/'
channel1id = 373488574219157507
channel2id = 405215974745440266
@client.event #ログイン・認証
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_ready():
    print("-"*20)
    print("ユーザー名：", client.user.name)
    print("ユーザーID：", client.user.id)
    print("-"*20)

@client.event
async def on_message(message):
   if(message.channel.name == "general" or message.channel.name == "block-rewards-chat"):
        if message.author.id != client.user.id:
            channel_jpbot = [channel for channel in client.get_all_channels() if channel.name == 'japanese'][0]
            url = 'https://translate.google.com/?hl=ja#en/ja/'
            r = requests.get(url, params={'q': message.content})
            pattern = "TRANSLATED_TEXT=\'(.*?)\'"
            result = re.search(pattern, r.text).group(1)
            string = "チャンネル: " + message.channel.name + "\n" + "投稿者: " + message.author.name + "\n" + "メッセージ: " + result
            await client.send_message(channel_jpbot, string)
        print("channel id:", message.channel.id)
        print("投稿しました")
        print("チャンネル:", message.channel)
        print("投稿者：", message.author)
        print("メッセージ：", message.content)

client.run("YOURTOKEN")
