import sys

# txtファイルの読み込み
def txt_load():
    file = open('../articles/HelloWorld.txt', 'r')
    data = file.read().casefold()
    file.close()
    return data

# キーワードを含むか判定  
def check_keyword(key_word):
    search_file = txt_load()
    if key_word in search_file:
        result = "TRUE"
    else:
        result = "FALSE"
    print("Result: " + result)


if __name__ == "__main__":
    #検索キーワード入力
    input_word = sys.argv
    input_word = input_word[1]
    searching = f'Searching for "{input_word}" in HelloWorld.txt'
    print(searching)
    check_keyword(input_word)

