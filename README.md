**THIS IS A SAMPLE CODE FOR DISCORD BOT READ ALOUD　※ IT CAN BE USE JAPANESE ONLY**

## 【日本語】

ご覧いただきありがとうございます。
Discordボイスチャンネルでテキストを読み上げるBotです。

pyttsx3を使用しています。

pyttsx3はPythonのテキスト読み上げエンジンであり、ローカルの音声合成エンジンを使用してテキストを音声に変換します。
pyttsx3はGoogleのText-to-Speech APIに依存せず、ローカルで動作するため、インターネット接続が不要です。

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


 ## **導入方法**

以下の手順に従って、このBotを導入してください。

**1. 必要なソフトウェアのインストール**

まず、以下のソフトウェアをインストールしてください。

・Python: Discord Botを実行するために必要です。

・pip: Pythonパッケージの管理ツールです。

**2. プログラムのダウンロード**

GitHubからプログラムをダウンロードします。ダウンロード方法は次のとおりです。


1. GitHubで新しいリポジトリを作成してください。
2. 作成したリポジトリに移動し、「Code」ボタンをクリックします。
3. 「Download ZIP」を選択して、プログラムのZIPファイルをダウンロードします。
4. ダウンロードしたZIPファイルを解凍し、プログラムのフォルダを任意の場所に保存します。


**3. 必要なパッケージのインストール**

コマンドプロンプトまたはターミナルを開き、
以下のコマンドを実行して必要なパッケージをインストールします。


```bash 
pip install discord.py gtts pyttsx3 python-dotenv
```


**4. Discord Botの作成とトークンの取得**

Discordの開発者ポータルでBotを作成し、
Botのトークンを取得してください。以下の手順で行います。


1. Discord Developer Portalにアクセスし、ログインしてください。
2. 「New Application」をクリックして新しいアプリケーションを作成します。
3. 作成したアプリケーションのページで、左側のメニューから「Bot」を選択し、「Add Bot」ボタンをクリックします。
4. Botの設定を行い、トークンを取得します。]

**5. 環境変数の設定**

プログラムのフォルダに .env という名前のファイルを作成し、以下の内容を追加して保存してください。

```makefile
TOKEN=取得したトークン
```

このファイルには、取得したBotのトークンを設定します。


**6. Botの起動**

コマンドプロンプトまたはターミナルで、プログラムのフォルダに移動して以下のコマンドを実行してください。

```bash
python プログラムのファイル名.py
```

Botが起動し、Discordサーバーにオンライン状態として表示されます。

Botを使用してDiscordサーバーでコマンドを試してみてください。Botが正常に動作している場合、コマンドに応じた処理が実行されます。

以上で、Botの導入が完了しました。



## 【English】

Thank you for checking this out. This is a Discord bot that reads text aloud in voice channels. Below are the main functionalities of the bot.

**/name_hello command:**
Greets you by calling your name.
Usage: /name_hello [name]

**/hello command:**
Displays a message explaining how to use the bot.

**/join command:**
Connects to a voice channel.

**/leave command:**
Disconnects from the voice channel.

**/say command:**
Reads the input text aloud.
Usage: /say [text]

**/dictionary command:**
Registers a word in the dictionary.
Usage: /dictionary [word] [reading]

**/dictionary_list command:**
Displays a list of words registered in the dictionary.

**/member_list command:**
Displays a list of members in the voice channel.

## **Installation Guide**

Please follow the steps below to install this bot.

**1. Install Required Software**

First, install the following software:

Python: Required to run the Discord bot.
pip: Package management tool for Python.

**2. Download the Program**

Download the program from GitHub using the following steps:

1. Create a new repository on GitHub.
2. Navigate to the repository and click the "Code" button.
3. Select "Download ZIP" to download the program as a ZIP file.
4. Extract the downloaded ZIP file and save the program folder in the desired location.

**3. Install Required Packages**

Open the command prompt or terminal and execute the following command to install the required packages:

```bash
pip install discord.py gtts pyttsx3 python-dotenv
```

**4. Create a Discord Bot and Obtain Token**

Create a bot on the Discord Developer Portal and obtain the bot token using the following steps:

1. Access the Discord Developer Portal and login.
2. Click "New Application" to create a new application.
3. In the created application's page, select "Bot" from the left menu and click the "Add Bot" button.
4. Configure the bot and obtain the token.

**5. Set Environment Variables**

Create a file named .env in the program folder and add the following content:

```makefile
TOKEN=your_token_here
```

Set your bot token obtained from the previous step as the value for TOKEN.


**6. Start the Bot**

Navigate to the program folder using the command prompt or terminal and execute the following command:

```bash
python program_filename.py
```


The bot will start and appear online on your Discord server.

Test the bot by using the commands on your Discord server. If the bot is functioning correctly, it will execute the appropriate actions based on the commands.

That's it! The installation of the bot is now complete.


## 作成者 Bot developer

- 作成者: Paraccoli
- GitHub: (https://github.com/paraccoli)

