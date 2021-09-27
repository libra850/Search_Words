import sys
import glob
import os.path

# 検索文
def sentence(key_word):
    loading_sentence = f'Searching for "{key_word}"'
    print(loading_sentence)
    print("Results:")

# articlesフォルダーの読み込み
def folder_load():
    files_dict = {}
    for file in glob.glob('../articles/*.txt'):
        article = open(file, "r")
        article_title = os.path.splitext(os.path.basename(file))[0]
        article_contents = article.read().casefold()
        files_dict[article_title] = article_contents
        article.close()
    return files_dict

# キーワードを含む記事の抽出 
def abstract_articles(key):
    articles_data = folder_load()
    index_num = 0
    total = 0
    for title,contents in articles_data.items():
        if key in contents:
            index_num += 1
            total += 1
            article_result = f'{index_num}. {title}'
            print(article_result)
    print("")
    print("Total: ",total)


if __name__ == "__main__":
    # 検索ワード有無の確認
    try:
        input_word = sys.argv[1].casefold()
    except IndexError:
        print("Error: 検索キーワードが入力されていません")
        exit()
    sentence(input_word)
    abstract_articles(input_word)
    
