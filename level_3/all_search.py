import sys
import glob
import os.path

# 検索文
def load(key_word):
    loading_sentence = f'Searching for "{key_word}"'
    print(loading_sentence)
    print("Results:")
    
def check_keyword(key):
    index_num = 0
    total_num = 0
    # 全ファイルの読み込み
    for files in glob.glob('../articles/*.txt'):
        articles = open(files, "r")
        key_words_data = articles.read().casefold()
        articles.close()
        # キーワード検索
        if key in key_words_data:
            index_num += 1
            total_num += 1
            article_name = os.path.splitext(os.path.basename(files))[0]
            result = f'{index_num}. {article_name}'
            print(result)
    print("")
    print(f'Total: {total_num}')

if __name__ == "__main__":
    try:
        input_word = sys.argv[1].casefold()
    except IndexError:
        print("Error: 検索キーワードが入力されていません")
        exit()
    load(input_word)
    check_keyword(input_word)