from collections import Counter
import csv

from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
corpus = []

print('辞書読み込み中...')
bow_data = {}
with open(r"C:\Users\***\Desktop\そつけん\src\resultRep_dct.csv", encoding="sjis") as f:
    reader = csv.DictReader(f)
    for row in reader:
        corpus.append(row["resultRepList"])
        """
        bow_data[row["Name"]] = {
            "count_data": Counter(row["resultRepList"].split(' '))
        }
        # print(bow_data[row["Name"]])
        """

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)
print(vectorizer.get_feature_names())
print(X.toarray())

def get_tfidf_and_feature_names(corpus):
    vectorizer = TfidfVectorizer(token_pattern=u'(?u)\\b\\w+\\b')
    return vectorizer.fit_transform([text for text in corpus]), vectorizer.get_feature_names()

w, feature_names = get_tfidf_and_feature_names(corpus)
word_vectors='yasu suki iya yasu yasu suki iya yasu yorokobi yasu yasu'

v = np.asarray([word_vectors(word) for word in feature_names])

"""
# input_data = "yasu suki iya yasu yasu suki iya yasu yorokobi yasu yasu"

input_data = ""

while input_data != "e":
    input_data = input("データを入力してください(終了はe):")

    input_counter = Counter(input_data.split(' '))

    # 結果格納用
    result_set = []
    for songName, data in bow_data.items():
        tmp_score = 0
        # ある曲についてのCounterを取得
        count_data = data["count_data"]
        # print(count_data)
        # 抽出した感情を1つずつ取得
        for word, word_count in input_counter.items():
            # ある曲の感情の出現数と入力したデータの感情の出現数を乗じてスコアに加算
            tmp_score += count_data.get(word, 0) * word_count
        # scoreが0なものは候補から外す
        if tmp_score == 0:
            continue
        result_set.append({
            "songName": songName,
            "score": tmp_score
        })
        # print("songName: " + songName + ", score: " + str(tmp_score))

    # スコアの降順で整列
    result_set.sort(key=lambda x: x["score"], reverse=True)

    # 上位5件を取得
    for result in result_set[:10]:
        print(result)
"""