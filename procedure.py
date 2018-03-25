1.バックアップを実行するユーザーを作成
# backup_user とか
Access key ID,Secret access key を DL

backup_user 用 プロファイルを使って aws CLI に上記キーをセット
# aws configure --profile backup_user

pipenv インストール
# pip3 install pipenv

バージョン 3 にして
# pipenv --three

boto3 と ipython をインストール
# pipenv install boto3
# pipenv install -d ipython

pipenv で ipython を開く
# pipenv run ipython

boto3 で、backupuser を指定して Session を開く
# session = boto3.Session(profile_name='backupuser'

session で、ec2 サービスを取得
# ec2 = session.resource("ec2")

全 EC2 インスタンスを取得して、出力
# for i in ec2.instances.all():print(i)
# (UnauthorizedOperation) エラー

コンソールから backupuser ユーザーに EC2 のフルアクセスを与える

ヒストリーから、使用したコマンドをコピー →ipython を抜ける

ipython で使用感を試したあとで、それをモジュールにする
# vi backup_ami.property

click をインストール
# pipenv install click

click で コードをデコレート
--help を引数につけるとヘルプが表示されるようになる
# @click.command()
# pipenv run "backup_ami\backup_ami --help"

Doc String をファンクションにつけてみる
 # → --help をつけた時のヘルプ文字列になる
# def list_instances():
#     # Doc string
#     "List EC2 instances"

boto3 の ファンクションの参照方法
ipython に入る
boto3 をインポート
対象サービスのセッションを設定
ec2 の 全 instance を 変数に格納
# inst = ec2.instances.all()
インスタンスリストの要素を一つ取り出して、どんな情報があるかみてみる

このデータ型はなんなんだ？
type(inst)
# boto3.resources.collection.ec2.instancesCollection

リストコンストラクタに渡して出力
# list(inst)

問題ない？っぽいので、リストから要素を一つ取り出し、変数に割り当てる
# i = list(inst)[0]
# で、どんな key/value があるか探索できる

フィルター作成(リスト内に辞書構造)
# filters = [{'Name': 'tag:Project', 'Values':["valkyrie"]}]

backup_ami.py の使い方
-------------------------------------------------
インスタンス情報を出力
# pipenv run "backup_ami\backup_ami"
指定したプロジェクト名のインスタンス情報を出力
pipenv run "backup_ami\backup_ami --project=Valkyrie"
-------------------------------------------------

ec2 の タグ 情報を、"Dictionary Comprehension" でリスト形式から辞書形式に変換
# boto3 で ec2 OBJ を作成し、全インスタンス情報を取得
# 調査用に最初の要素を引き出す
# i = list(instances)[0]
# tags = {}
# 右側で for ループして t に格納
# t から "Key のvalue": "Value のvalue" みたく辞書形式にデータを整形し、変数に格納
tags = { t['Key']: t['Value'] for t in i.tags or []}

インスタンス情報経由で EBS 情報を取得
 from backup_ami import backup_ami
 project = 'Valkyrie'
instances = backup_ami.filter_instances(project)
for i in instances:
    print(i)
    for v in i.volumes.all():
        print(v)
