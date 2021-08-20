from collections import Counter
import csv

print('辞書読み込み中...')
bow_data = {}
with open(r"C:\Users\***\Desktop\そつけん\src\resultRep_dct_akg.csv", encoding="sjis") as f:
    reader = csv.DictReader(f)
    for row in reader:
        bow_data[row["Name"]] = {
            "count_data": Counter(row["resultRepList"].split(' '))
        }

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

    # スコアの降順で整列
    result_set.sort(key=lambda x: x["score"], reverse=True)

    # 上位5件を取得
    for result in result_set[:10]:
        print(result)