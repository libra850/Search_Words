import sys

# txtファイルの読み込み
def txt_load():
    file = open('../articles/HelloWorld.txt', 'r')
    data = file.read().casefold()
    file.close()

    return data

search_file = txt_load()

# キーワードを含むか判定  
def check_keyword():
    key_word = sys.argv
    key_word = key_word[1].casefold()

    searching = f'Searching for "{key_word}" in HelloWorld.txt'
    print(searching)

    if key_word in search_file:
        result = "TRUE"
    else:
        result = "FALSE"
    print("Result: " + result)


if __name__ == "__main__":
    check_keyword()
