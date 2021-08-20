from bs4 import BeautifulSoup

import requests
import time
import re
import os

# 歌手の歌詞リストのURL
url = "https://j-lyric.net/artist/a060ee9/"

# 保存先
location = r'C:\Users\***\歌詞'

# 楽曲URL抽出部分
songUrl_list = []
r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")
song_list = soup.select('a[href]')

for song in song_list:
    songurl = re.sub(r'^(?!.*artist).*$', '', song.get('href'))
    songurl = re.sub(r'^/artist/.*/', url, songurl)
    songurl = songurl.replace(r'/artist/p1.html', '')
    if songurl: songUrl_list.append(songurl)

# 歌詞抽出部分
i = 0
for songUrlLi in songUrl_list:
    # デバッグ用 取得回数記録・表示
    i += 1
    print(i)

    url = str(songUrlLi)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    
    # 改行コードを改行に置換
    for brc in soup.select("br"):
        brc.replace_with("\n")
    
    # 必要のないタグを削除して曲名と歌手名を抽出
    wordlist = [x.text for x in soup.find_all(id="Lyric")]

    songName = [x.text for x in soup.find('div', class_='cap')]
    songName = re.findall(r'\「(.*)\」歌詞', songName[0])
    songName = re.sub(r'[\\\/\:\%\#\$\&\?\(\)\~\.\=\+\-\…]', "", songName[0])

    singerName = [x.text for x in soup.find('div', class_='lft')]
    singerName = re.sub(r'[\\\/\:\%\#\$\&\?\(\)\~\.\=\+\-\…]', "", singerName[0])
    singerName = re.findall(r'^(.*) '+ songName + ' 歌詞', singerName)
    singerName = singerName[0]
    
    # 曲名+歌手名の表示
    print(str(songName) + ' / ' + str(singerName))
 
    # 書き込み先ディレクトリ
    writeDir = location + '\\' + singerName + '\\'
    
    # ディレクトリが存在しない場合、ディレクトリを作成する
    if not os.path.exists(writeDir):
        os.makedirs(writeDir)

    # 楽曲毎のファイルに歌詞を保存
    for word in wordlist:
        lyric = re.sub('\(.+?\)', "", str(word))
        with open(writeDir + songName + '.txt', 'w') as f:
            f.write(lyric)
    f.close()
    
    # DoS回避
    time.sleep(2)