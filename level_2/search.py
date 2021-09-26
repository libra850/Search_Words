import sys

# 検索文
def load(key_word):
    searching = f'Searching for "{key_word}" in HelloWorld.txt'
    print(searching)

# txtファイルの読み込み
def txt_load():
    file = open('../articles/HelloWorld.txt', 'r')
    words_data = file.read().casefold()
    file.close()
    return words_data

# キーワードを含むか判定  
def check_keyword(key,target_file):
    if key in target_file:
        result = "TRUE"
    else:
        result = "FALSE"
    print("Result: " + result)


if __name__ == "__main__":
    #検索キーワード入力
    try:
        input_word = sys.argv[1].casefold()
    except IndexError:
        print("Error: 検索キーワードが入力されていません")
        exit()
    load(input_word)
    txt_data = txt_load()
    check_keyword(input_word,txt_data)