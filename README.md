# Coding_Test

## 実装コードの使い方
__<概要>__<br>
・リモートリポジトリのclone<br>
・Dockerの起動方法<br>
・Level_2のコード使用方法<br>
・Level_3のコード使用方法<br>
・Dockerの終了方法

-----------------------------------------------------------
__＜リモートリポジトリのclone＞__
1. ターミナルを起動してcloneするディレクトリに移動（eg:デスクトップ）

2. ターミナルにて下記コードをペーストしてください
``` terminal.rb
git clone git@github.com:libra850/Coding_Test.git
```
3. パスワードを求められるので下記にあるパスワードを入力
```
Enter passphrase for key '/Users/motokisugitani/.ssh/id_rsa':
-------------------------------------------------------------
上記のメッセージが表示されるのでパスを入力してください 
```
__PASSWORD（公開鍵）: kfoamfjaope749137__

4. カレントディレクトリからCoding_Testフォルダーに移動してください
```
desktop % cd Coding_Test
      ↓
Coding_Test % 
```

-----------------------------------------------------------
__＜Dockerの起動＞__
1. 下記のコマンドをターミナル内で入力してください
```
docker-compose up --build -d
-----------------------------------------------------------
REPOSITORY            TAG       IMAGE ID       CREATED        SIZE
coding_test_python3   latest    b26c0edaf588   3 hours ago    1GB
```    
※上記の結果が出力されます

2. 確認できたら次にこのコマンドを入力してください
```
docker compose exec python3 bash
```

下記の内容が表示されます
```
Coding_Test % docker compose exec python3 bash

root@4a6bb0506f2e:~#
```
lsコマンドで下記フォルダーがあることを確認できます
```
Coding_Test % docker compose exec python3 bash

root@4a6bb0506f2e:~# ls
articles  level_2  level_3
```
-----------------------------------------------------------
__＜Level_2のコード使用方法＞__
```
cd level_2
```
1. 下記コマンドをターミナルで実行してください
```
python search.py <調べたい単語>
```
例：
```
python search.py ICC

Searching for "icc" in HelloWorld.txt
Result: TRUE
```
-----------------------------------------------------------
__＜Level_3のコード使用方法＞__
```
cd level_3
```
1. 下記コマンドをターミナルで実行してください
```
python all_search.py <調べたい単語>
```
例：
```
python search.py ICC

Searching for "icc" in HelloWorld.txt
Result: TRUE
```
-----------------------------------------------------------
__＜Dockerの終了方法＞__
```
exit
```
```
docker compose stop
```
下記の状態になっていれば終了です
```
docker compose ls
--------------------------
NAME                STATUS
```