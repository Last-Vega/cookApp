# cookApp

## Flask + Vue

## 構成
- backend
  - FlaskでAPIを作成
  - ルート直下のdist(Vueでビルドしたフォルダ)をテンプレートフォルダにしている。
  - ルート直下のrequirements.txtを元にpythonのパッケージをインストールする。
- frontend
  - Vueでフロントを作成
- postgres
  - PostgreSQLの初期化ファイルが置かれ、コンテナ起動時に実行される。
- manage.py
  - Flaskサーバーを起動する処理を記述
  - コンテナ起動時に実行される。
- docker-compose.yml
  - コンテナ起動時の設定ファイル
- Dockerfile_***
  - イメージの設定ファイル  

## 最初にすること
- frontend直下に.env.localを置き、'VUE_APP_BASE_URL=<コンテナが起動しているOSのIPアドレス>:5000/'を記述する。
  【例】
    ```
    VUE_APP_BASE_URL=http://localhost:5000/
    ```
- ルートディレクトリでdocker-compose buildを実行してイメージを作成する。
  - backend
    - requirements.txtの内容でpip installが走る。
  - frontend
    - package.jsonの内容でnpm installが走る。
    - npm run buildが実行され、Vueのdistフォルダがルート直下に作成される。

## 毎回すること
- ルートディレクトリでdocker-compose up (バックグランドで実行する場合は '-d'を付ける。)を実行してコンテナを起動する。
  - backend
    - manage.pyが実行され、Flaskサーバーが立ち上がる。
    - コンテナが起動しているOSのIPアドレス:5000でサービスにアクセスできる。
    【例】
      ```
      localhost:5000/
      ```
  - postgres
    - PostgreSQLが起動する。
    - コンテナを起動させた状態で別のターミナルからpostgresでSQLを叩きたいとき
    ```
    docker-compose exec postgres bash
    psql -U root -h postgres -d cookapp
    ```

    でpostgresコマンドを叩ける
- フロントの開発をするときには、通常通りホストマシン上でnpm run serve でローカルサーバーを立ち上げ、ビルドするときはnpm run build

## デプロイするとき
- Dockerイメージを用いてデプロイする
### 手順
1. masterの内容をdeployブランチにpullする
  - GitHub Desktopなら
    - masterブランチで `Fetch origin` で最新のものをpullする
    - deployブランチに移動し, branch->`Update from master`を選択
  - コマンドラインなら(合ってるかわからない...)
  ```
  git checkout master # masterブランチに移動
  git pull origin master # masterを更新
  git checkout deploy # deployブランチに移動
  git merge master # マスターをマージ
  ```

2. herokuにログイン
  ```
  heroku login
  ```

3. アプリ作成(初回のみ)
  ```
  heroku create [アプリ名]
  ```

4. Container Registry にログイン
```
heroku container:login
```

5. Dockerイメージのビルド・プッシュ
  ```
  heroku container:push web
  ```

6. Dockerイメージのリリース
  ```
  heroku container:release web
  ```

7. 動作確認
  ```
  heroku open
  ```

## その他使うコマンド
- npmやpipのパッケージを更新した時には、変更を反映させるためにdocker-compose up --build (-d)でビルド&コンテナ起動するようにする。
