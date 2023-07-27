import discord
from discord.ext import commands
from gtts import gTTS
import pyttsx3
import asyncio
import os
from dotenv import load_dotenv

load_dotenv("YOUR_.env_FILE_PASS_HERE")

TOKEN = os.getenv('TOKEN')

# デフォルトの音声合成エンジンを設定
current_engine = "gtts"

# 絵文字リアクションの定義
emoji_gtts = "🇬"
emoji_pyttsx3 = "🇵"

if TOKEN is None:
    raise ValueError('.envfileにTOKENがありません')

client = commands.Bot(command_prefix='/')

#ログイン
@client.event
async def on_ready():
    print("on_ready")
    # play Project DIVA
    await client.change_presence(activity=discord.Game("SampleGame"))


#名前を呼んで挨拶
@client.slash_command(description="このコマンドはあなたの名前を呼んであいさつします！")
async def name_hello(ctx, name):
    await ctx.respond(name + "さんこんにちはー")



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
