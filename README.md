# XML単語カウンター

このPythonツールは、指定されたフォルダ内の最新のXMLファイルから、指定された単語の出現回数をカウントします。  
結果はテキストファイル (.txt) と Excelファイル (.xlsx) で出力できます。

## 特徴

*   **XMLファイル解析**: XMLファイルを読み込み、テキストデータを抽出します。
*   **キーワード検索**: ユーザーが指定したキーワードを、大文字小文字を区別せずに検索します。
*   **最新ファイル処理**: 指定したフォルダ内の最新のXMLファイルを自動的に選択して処理します。
*   **柔軟な出力形式**: 結果を、カンマ区切り形式のテキストファイル (.txt) または Excelファイル (.xlsx) で出力できます。
*   **ファイルの上書き防止**: 出力ファイル名が重複する場合、自動的に連番を付与し、上書きを防ぎます。

## 使い方

1.  **このリポジトリをローカルにコピーする:**
    *   以下のコマンドをターミナル（またはコマンドプロンプト）で実行してください。
       ```bash
       git clone <リポジトリのURL>
       ```
       *   `<リポジトリのURL>` には、このリポジトリのGitHubページのURL（例:`https://github.com/yourusername/your-repo-name.git`）を貼り付けてください。


2.  **Pythonとライブラリのインストール:**
    *   Python 3.6以上が必要です。必要であれば、[https://www.python.org/](https://www.python.org/) からインストールしてください。
    *   `pandas` と `openpyxl` ライブラリが必要です。以下のコマンドでインストールできます。
        ```bash
        pip install pandas openpyxl
        ```
    * Anaconda環境を利用している場合は、`conda install pandas openpyxl` でインストールできます。

3.  **XMLファイルの準備:**
    *   解析したいXMLファイルを、 `./content/xml_files` という名前のフォルダを作成し、その中に配置します。
4.  **Pythonスクリプトの実行:**
    *   ターミナル（コマンドプロンプト）で、Pythonスクリプトを実行します。
    *   実行時に、XMLファイルへのパスと、検索したい単語をスペース区切りで入力します。

5.  **結果の確認:**
    *   スクリプトを実行すると、`./content/word_counts` フォルダに、テキストファイルとExcelファイルが生成されます。
    *  テキストファイルには、`単語,出現回数`の形式で出力されます。



## 【サンプル】入力文
```
単語A 単語B
```

## 【サンプル】出力ファイル
テキストの場合
```
単語,出現回数
単語A,23
単語B,4
```

Excelの場合
![image](https://github.com/user-attachments/assets/dd077da1-472d-482a-81a3-720e41d653a3)


## 動作環境

*   Python 3.6以上
*   `pandas`
*   `openpyxl`

## 注意事項

*   指定されたフォルダ内にXMLファイルが存在しない場合、エラーが表示されます。
*   XMLファイルの構造によっては、期待通りに単語を抽出できない場合があります。
*   テキストファイルの文字コードはUTF-8です。

