#ライブラリ
import discord
from discord.ext import commands
import logging
from config import admin_account_id


#一般ライブラリ
import json
import time
import random
import datetime
import re

#音声ライブラリ
from gtts import gTTS
import pyttsx3
import asyncio
import os
from dotenv import load_dotenv

load_dotenv(".env")

TOKEN = os.getenv('TOKEN')

# デフォルトの音声合成エンジンを設定
current_engine = "gtts"

# 絵文字リアクションの定義
emoji_gtts = "🇬"
emoji_pyttsx3 = "🇵"

if TOKEN is None:
    raise ValueError('.envfileにTOKENがありません')

client = commands.Bot(command_prefix='/', description = "This bot is made by Paraccoli", ower_id = 957169126990827520)

# ログファイルのパス
log_file_path = "log.txt"

# ログの設定
logging.basicConfig(filename=log_file_path, level=logging.DEBUG)


#Loginfo
@client.slash_command(description="このコマンドは管理者専用です！")
async def loginfo(ctx):
    # ログチャンネルのIDを指定
    log_channel_id = 1181620524774850761
    log_channel = client.get_channel(log_channel_id)

    sender_id = ctx.author.id

    # 特定のアカウントIDと比較
    if sender_id == admin_account_id:
        if log_channel:
            try:
                with open(log_file_path, 'rb') as file:
                    await log_channel.send(file=discord.File(file, 'log.txt'))
            except FileNotFoundError:
                print("ログファイルが見つかりません。")
        else:
            print("ログチャンネルが見つかりません。")
    else:
        embed = discord.Embed(title="デバックログ", description="ログを表示します。", color=discord.Color.green())
        embed.add_field(name="/loginfo",value="あなたは管理者ではありません。このコマンドは管理者のみ使用できます。", inline=False)
        await ctx.respond(embed=embed)


#ログイン
@client.event
async def on_ready():
    print("on_ready")
    # play Project DIVA
    await client.change_presence(activity=discord.Game("Project DIVA"))

    # ログの設定
    logging.basicConfig(level=logging.DEBUG)  # DEBUG レベル以上のログを表示

    # デバッグメッセージ
    logging.debug("on_ready")

    # ボット情報の表示
    print(f'-----------------------------')
    print(f'完了しました。')
    print(f"{client.user.name}にログインしました。")
    print(f"ID: {client.user.id}")
    print(f"サーバー数: {len(client.guilds)}")
    print(f"参加メンバー数: {len(client.users)}")
    print(f'-----------------------------')

    # インフォメーションメッセージ
    logging.info("ログインしました。")
    logging.info(f"ID: {client.user.id}")
    logging.info(f"サーバー数: {len(client.guilds)}")
    logging.info(f"参加メンバー数: {len(client.users)}")

    # ワーニングメッセージ
    logging.warning("これは警告メッセージです")

    # エラーメッセージ
    logging.error("これはエラーメッセージです")

    # 終了時のログメッセージ
    logging.info("Received signal to terminate bot and event loop.")
    logging.info("Cleaning up tasks.")
    logging.info("Cleaning up after 1 tasks.")
    logging.info("All tasks finished cancelling.")
    logging.info("Closing the event loop.")



#名前を呼んで挨拶
@client.slash_command(description="このコマンドはあなたの名前を呼んであいさつします！")
async def name_hello(ctx, name):
     if name == "Paraccoli": 
        embed = discord.Embed(title= name +"さんこんにちは！", description="デバックLOGを表示します。", color=discord.Color.blue())
        embed.add_field(name="/loginfo",value="", inline=False)
        await ctx.respond(embed=embed)
     else:
        embed = discord.Embed(title= name +"さんこんにちは！", description="私の使い方を知りたいですか？", color=discord.Color.green())
        embed.add_field(name="/hello", value="このコマンドで使い方を説明しますよ！", inline=False)
        await ctx.respond(embed=embed)

#使い方の説明
@client.slash_command(description="このコマンドはこのBotの使い方を説明します！\n使用方法：/hello")
async def hello(ctx):
    embed = discord.Embed(title="読み上げボットです！", description="下記のコマンドを試してみてね！", color=discord.Color.green())
    embed.add_field(name="/join", value="ボイスチャンネルに接続するよ！", inline=False)
    embed.add_field(name="/leave", value="ボイスチャンネルを切断するよ！", inline=False)
    embed.add_field(name="/say", value="入力したテキストを読み上げるよ！\n使用方法：/say [テキスト] [言語コード（省略可）]", inline=False)
    embed.add_field(name="/dictionary", value="単語を辞書に登録するよ！\n使用方法：/dictionary [単語] [読み方]", inline=False)
    embed.add_field(name="/dictionary_list", value="辞書に登録された単語一覧を表示するよ！", inline=False)
    embed.add_field(name="/member_list", value="ボイスチャンネル内のメンバー一覧を表示するよ！", inline=False)
    embed.set_thumbnail(url='https://image.gif')
    embed.set_image(url='https://giffiles.url')
    await ctx.respond(embed=embed)


#ボイスチャンネルに接続
@client.slash_command(description="このコマンドはボイスチャンネルに接続します！")
async def join(ctx):
    if ctx.author.voice is None:
        await ctx.send("ボイスチャンネルに接続してから実行してね！")
    voice_channel = ctx.author.voice.channel
    await voice_channel.connect()
    await ctx.send("接続しました！")


#ボイスチャンネルから退出
@client.slash_command(description="このコマンドはボイスチャンネルから退出します！")
async def leave(ctx):
    voice_client = ctx.guild.voice_client
    if voice_client is None:
        await ctx.send("ボイスチャンネルに接続していないよ！")
    else:
        await voice_client.disconnect()
        await ctx.send("退出しました！")



# 辞書機能の追加
word_dictionary = {}

@client.slash_command(description="このコマンドは単語を辞書に登録します！")
async def dictionary(ctx, word: str, reading: str):
    global word_dictionary
    if word in word_dictionary:
        await ctx.send("その単語はすでに辞書に登録されています。")
    else:
        word_dictionary[word] = reading
        await ctx.send(f"{word}を辞書に登録しました！")

@client.slash_command(description="このコマンドは辞書に登録された単語一覧を表示します！")
async def dictionary_list(ctx):
    global word_dictionary
    if not word_dictionary:
        await ctx.send("辞書に登録された単語はありません。")
    else:
        words = "\n".join([f"{word}: {reading}" for word, reading in word_dictionary.items()])
        embed = discord.Embed(title="辞書に登録された単語一覧", description=words, color=discord.Color.green())
        await ctx.send(embed=embed)



#ボイスチャンネルメンバー表示
@client.slash_command(description="このコマンドはボイスチャンネル内のメンバー一覧を表示します！")
async def member_list(ctx):
    voice_channel = ctx.author.voice.channel
    if voice_channel is None:
        await ctx.send("ボイスチャンネルに接続してから実行してね！")
        return
    
    members = voice_channel.members
    member_names = [member.name for member in members]
    if not member_names:
        await ctx.send("ボイスチャンネルにはメンバーがいません。")
    else:
        member_list_str = "\n".join(member_names)
        embed = discord.Embed(title="ボイスチャンネルのメンバー一覧", description=member_list_str, color=discord.Color.green())
        await ctx.send(embed=embed)


@client.slash_command(description="このコマンドはテキストを読み上げます！")
async def say(ctx, text):
    # ボイスチャンネルに接続しているか確認する
    voice_client = ctx.guild.voice_client
    if voice_client is None:
        await ctx.send("ボイスチャンネルに接続していないよ！")
        return
    
    # テキストを音声ファイルに変換する
    tts = gTTS(text=text, lang='ja')
    tts.save('voice.mp3')
    
    # 音声ファイルを再生する
    vc = voice_client
    source = discord.FFmpegPCMAudio('voice.mp3')
    vc.play(source)
    while vc.is_playing():
        await asyncio.sleep(1)
    vc.stop()
    os.remove('voice.mp3')
    await ctx.send(text)
    print(text)



client.run(TOKEN)
