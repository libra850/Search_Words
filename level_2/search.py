import sys

# 検索文
def sentence(key_word):
    loading_sentence = f'Searching for "{key_word}" in HelloWorld.txt'
    print(loading_sentence)

# HelloWorld.txtの読み込み
def file_load():
    article = open('../articles/HelloWorld.txt', 'r')
    article_contents = article.read().casefold()
    article.close()
    return article_contents

# キーワードを含むか判定  
def check_keyword(key):
    article_data = file_load()
    if key in article_data:
        result = "TRUE"
    else:
        result = "FALSE"
    print("Result: " + result)


if __name__ == "__main__":
    #検索キーワード入力
    input_word = sys.argv[1].casefold()  
    sentence(input_word)
    check_keyword(input_word)