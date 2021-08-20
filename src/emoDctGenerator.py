import mlask
import os
from glob import glob
import csv

"""
# mecab-ipadic-neologdをインストールしてないので使えない
cmd='echo `mecab-config --dicdir`"/mecab-ipadic-neologd"'
path = (subprocess.Popen(cmd, stdout=subprocess.PIPE,
                           shell=True).communicate()[0]).decode('utf-8')
                           
emotion_analyzer = mlask.MLAsk('-d {0}'.format(path))  # Use other dictionary
"""

dir_name = r'C:\Users\***\歌詞\ASIAN KUNGFU GENERATION'

emotion_analyzer = mlask.MLAsk()
resultEmoAnl = list()

# 歌詞ファイルを全て読み込む
for path_name in glob(dir_name + r'\*.txt'):
	with open(path_name, mode='r') as f:
		list_text = f.read().splitlines()
	
	# 感情推定を行う
	emoAnlyzed = list(map(emotion_analyzer.analyze, list_text))

	# 感情推定結果を整形し、必要なものだけを抜き出す。
	resultRep = [d.get('representative') for d in emoAnlyzed]
	resultRepList = list()

	for item in resultRep:
		if not str(item) == 'None':
			resultRepList.append(str(item[0]))
	
	# 結果を記録
	resultEmoAnl.append({'Name': os.path.splitext(os.path.basename(path_name))[0], 'resultRepList': " ".join(resultRepList)})

# 作成した感情推定辞書をcsvファイルで保存
labels = ['Name', 'resultRepList']

try:
    with open('resultRep_dct_akg.csv', 'w', newline="") as f:
        writer = csv.DictWriter(f, fieldnames=labels)
        writer.writeheader()
        for elem in resultEmoAnl:
            writer.writerow(elem)
except IOError:
    print("I/O error")