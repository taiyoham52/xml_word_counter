import xml.etree.ElementTree as ET
import re
from collections import Counter
import pandas as pd
import os
import csv
import datetime

def count_words_from_xml(xml_file_path, search_words):
    """XMLファイルからテキストを抽出し、指定された単語の出現回数をカウントする関数"""
    try:
        tree = ET.parse(xml_file_path)
        root = tree.getroot()
        text = ""

        # XMLタグに応じてテキスト抽出処理を実装
        for elem in root.iter():
           if elem.text:
             text += elem.text + " "

        # タグを除去し、改行や空白を正規化
        text = re.sub(r'<[^>]*?>', ' ', text)
        text = re.sub(r'[\n\r\t]+', ' ', text)
        text = re.sub(r'\s+', ' ', text).strip()

        # カウント
        word_counts = {}
        for search_word in search_words:
            count = len(re.findall(rf'{re.escape(search_word.lower())}', text.lower()))
            word_counts[search_word] = count
        return word_counts

    except Exception as e:
        print(f"エラーが発生しました：{e}")
        return None

# ファイルをアップロードするフォルダを指定
target_dir = './content/xml_files'
os.makedirs(target_dir, exist_ok=True) #フォルダを作成

# フォルダ内のXMLファイルを取得
xml_files = [os.path.join(target_dir, f) for f in os.listdir(target_dir) if f.endswith('.xml')]

if not xml_files:
    print("指定されたフォルダ内にXMLファイルが見つかりませんでした。")
else:
    # 最新のファイルを取得
    latest_file = max(xml_files, key=os.path.getmtime)
    xml_file_path = latest_file
    print(f"最新のXMLファイル: {os.path.basename(xml_file_path)} を処理します。")



    # ユーザーからの入力を受け付ける
    search_text = input("検索したい単語をスペース区切りで入力してください: ")
    search_words = [word.lower() for word in search_text.split()] # 検索キーワードも小文字に変換

    # 単語のカウントを実行
    word_counts = count_words_from_xml(xml_file_path, search_words)

    if word_counts:
        # ファイル名の設定
        base_file_name = './content/word_counts' # XMLファイル名を含むように設定

        # 末尾の数値を決定
        counter = 1
        txt_file_path = f'{base_file_name}_{counter}.txt'
        while os.path.exists(txt_file_path):
            counter += 1
            txt_file_path = f'{base_file_name}_{counter}.txt'

        excel_file_path = f'{base_file_name}_{counter}.xlsx'
        while os.path.exists(excel_file_path):
            counter += 1
            excel_file_path = f'{base_file_name}_{counter}.xlsx'


        # テキストファイル出力
        txt_file_path = f'{base_file_name}_{counter}.txt'
        with open(txt_file_path, 'w', encoding='utf-8') as f:
          f.write("単語,出現回数\n")  # ヘッダーを追加
          for word, count in word_counts.items():
              f.write(f"{word},{count}\n") # カンマ区切り、改行


        # Excelファイル出力
        excel_file_path = f'{base_file_name}_{counter}.xlsx'
        df = pd.DataFrame(word_counts.items(), columns=['単語', '出現回数'])
        df.to_excel(excel_file_path, index=False)
