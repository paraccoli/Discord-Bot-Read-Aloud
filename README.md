**THIS IS A SAMPLE CODE FOR DISCORD BOT READ ALOUD**

〖JP〗

ご覧いただきありがとうございます。
Discordボイスチャンネルでテキストを読み上げるBotです。
以下にBotの主な機能を説明します。

**/name_hello コマンド:**
      あなたの名前を呼んで挨拶します。
      使用方法: /name_hello [名前]
      
**/hello コマンド:**
      Botの使い方を説明するメッセージを表示します。

**/join コマンド:**
      ボイスチャンネルに接続します。

**/leave コマンド:**
      ボイスチャンネルから退出します。

**/say コマンド:**
    入力したテキストを読み上げます。
    使用方法: /say [テキスト]

**/dictionary コマンド:**
    単語を辞書に登録します。
    使用方法: /dictionary [単語] [読み方]

**/dictionary_list コマンド:**
    辞書に登録された単語一覧を表示します。

**/member_list コマンド:**
    ボイスチャンネル内のメンバー一覧を表示します。


    導入方法
Pythonと必要なパッケージをインストールしてください。
以下のコマンドを実行してください。

```pip install discord.py gtts pyttsx3 python-dotenv```

Discordの開発者ポータルでBotを作成し、トークンを取得してください。
取得したトークンを .env ファイルに保存してください。ファイルの内容は以下のようになります。

```TOKEN=取得したトークン```

