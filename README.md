# Search_Words

## 実装コードの使い方
__<概要>__<br>
- リモートリポジトリのclone<br>
- コード使用方法<br>
      - Dockerを使用しない場合<br>
      - Dockerを使用する場合<br>
- Level_2のコード使用方法<br>
- Level_3のコード使用方法<br>
- Dockerの終了方法

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
__＜Dockerを使用しない場合＞__

1. cdコマンドを使い、level_2・level_3のフォルダーに移動してください
```
cd level_2　

cd level_3
```
移動したら下記に記載されている各フォルダー毎の説明を参照してください

-----------------------------------------------------------
__＜Dockerを使用する場合＞__
1. 下記のコマンドをターミナル内で入力してください
```
docker-compose up -d
```    

2. 次にこのコマンドを入力してください
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
$ python search.py ICC
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
$ python all_search.py icc
Searching for "icc"
Results:
1. Amir cleared to tour New Zealand after visa granted
2. HelloWorld
3. ICC admits tweaking draws put Pakistan India same grou
4. India replace injured Yuvraj with batsman Pandey
5. Ireland win toss put Bangladesh into b

Total:  5
```
-----------------------------------------------------------
__＜Dockerの終了方法＞__
```
root@697a25f717c2:~#　exit
exit
```
```
Coding_Test %  docker compose stop
```
下記の状態になっていれば終了です
```
Coding_Test %　docker compose ls
--------------------------
NAME                STATUS
```
