#FROMで指定したDockerイメージをベース様々なコマンドを入力
FROM python:3.7

#RUN（コマンドの実行）/flaskディレクトリの作成
RUN mkdir /flask
#ADD（ファイル/ディレクトリの追加）/flaskにrequirements.txtを追加
#requirements.txtはパッケージの名前とバージョンの一覧が記載されたもの
ADD requirements.txt /flask

#WORKDIR（作業ディレクトリの指定）
WORKDIR /flask
#RUN（コマンドの実行）Python3に一括インストールする
RUN pip3 install -r requirements.txt

#EXPOSE（外部に公開するポートを指定）
EXPOSE 5010

#CMD（コンテナの実行コマンド）docker runみたいなやつ
CMD ["flask","run","-p","5010","-h","0.0.0.0"]
