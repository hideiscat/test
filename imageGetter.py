'''
・入力したURLから、人間の顔が映っているものだけ画像をDLします
・必要な要素は以下です
  ・
  ・
  ・
'''


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
import datetime
# Tkinterライブラリをインポートする
import tkinter
import os
import urllib.request
import shutil
import cv2 as cv
import requests
import json
import pprint
from PIL import Image, ImageDraw, ImageFont

# フォルダ作成
def makefolder():
    # 開始メッセージ
    print("01_フォルダ作成を開始します")
    #作成するディレクトリのpathを指定
    make_dir_path = './tmp'
    #作成しようとしているディレクトリが存在するかどうかを判定する
    if os.path.isdir(make_dir_path):
        #既にディレクトリが存在する場合は消してから再作成する
        shutil.rmtree(make_dir_path)
        os.makedirs(make_dir_path)
    else:
        #ディレクトリが存在しない場合のみ作成する
        os.makedirs(make_dir_path)

    print("02_フォルダ作成を終了します")

# 指定されたURLから画像をDLする
def mainDef(urlInputField):
    # 開始メッセージ
    print("03_chromeのwindowをシークレットモードで開きます")

    # シークレットモードのオプションを準備
    option = Options()
    option.add_argument('--incognito') 
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=option)
    
    # シークレットモードでchromeからURLを開く
    driver.get(urlInputField.get())

    # 画面が描画されるまで少し待つ
    time.sleep(1)
    
    # 画像の情報を全て取得
    menuLists = driver.find_elements(By.TAG_NAME, "img")
    
    # 画像の数を調べる
    print(len(menuLists))
    print(menuLists[0].get_attribute('src'))
    
    print("04_画像をDLします")

    # 画像を全てDL
    loopNumber = len(menuLists)
    for number in range(loopNumber) :
        print(menuLists[number].get_attribute('src'))

        # 余計なパラメータがついていたら、パラメータを削除する。
        imgFileName = os.path.basename(menuLists[number].get_attribute('src'))
        if '?' in imgFileName :
            imgFileName = imgFileName.split('?')[0]

        #同じファイル名対策として連番を付ける
        saveFileName = './tmp/'+ str(number).zfill(4) + '_' +imgFileName
        urllib.request.urlretrieve(menuLists[number].get_attribute('src'), saveFileName)

        # DLされるまで少し待つ
        time.sleep(1)

        # 画像の読み込み
        img = cv.imread(saveFileName)

    print("05_画像のDLを終了します")

##############################################
# 処理の開始                                  #
##############################################
# Tkinterインスタンスの生成
# 変数を使ってウィンドウの設定を行う
root = tkinter.Tk()
# ウィンドウのタイトルを指定する
root.title("サンプルプログラム")
# ウィンドウサイズを指定する。横×縦
root.geometry("640x80")


# 入力欄の作成はEntryを使用する。widthで幅を指定。
# URL
urlLabel = tkinter.Label(text='URL')
urlLabel.place(x=20, y=20)
urlInputField = tkinter.Entry(width=70)
urlInputField.place(x=160, y=20)

# ボタンクリック時に呼び出す関数を定義
def click_botton():
    #作業フォルダ作成
    makefolder()
    #メインメソッド
    mainDef(urlInputField)

# ボタンの作成はButtonを使用する。commandにて実行関数を指定する。
button = tkinter.Button(text="実行", command=click_botton)
# placeプロパティにて配置箇所をX,Y座標で指定する
button.place(x=20, y=40)

# ウィンドウの描画
root.mainloop()