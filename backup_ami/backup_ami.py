import boto3
import click

# backupuser プロファイルの AWS Access Key ID を使用するセッション
session = boto3.Session(profile_name='backupuser')
# 上記プロファイルでEC2 リソースを取得
ec2 = session.resource("ec2")

# 引数をもとにインスタンスをフィルタリングして返す
def filter_instances(project):
    instances = []

    if project:
        # Project タグが 引数のプロジェクトと一致するかどうかフィルタを定義
        filters = [{'Name': 'tag:Project', 'Values':[project]}]
        # リソースのうち、引数でフィルタリングされた結果のみ格納
        instances = ec2.instances.filter(Filters=filters)
    else:
        instances = ec2.instances.all()

    return instances


# ファンクションをグループ化
@click.group()
def instances():
    """Commands for instances"""

# backup_ami コマンド実行時の引数 list を与えると、下記が実行される
@instances.command("list")
# オプション、デフォルト、ヘルプ文言
@click.option('--project', default=None,
              help="Only instances for project (tag Project:<name>)")
def list_instances(project):
    # Doc string
    "List EC2 instances"

    instances = filter_instances(project)

    for i in instances:
        # リストでカプセル化された辞書を decapsulate して変数に格納
        tags = { t['Key']: t['Value'] for t in i.tags or []}
        print(', '.join((
            i.id,
            i.instance_type,
            i.placement['AvailabilityZone'],
            i.state['Name'],
            i.public_dns_name,
            i.image_id,
            # 右側はデフォ値
            tags.get('Project', '<no project>'))))

    return


@instances.command('start')
@click.option("--project", default=None,
              help='Only instances for project')
def start_instances(project):
    "Start EC2 instances"

    instances = filter_instances(project)

    for i in instances:
        print("Starting {0}...".format(i.id))
        # 対象 instance を停止
        i.start()

    return



@instances.command('stop')
@click.option("--project", default=None,
              help='Only instances for project')
def stop_instances(project):
    "Stop EC2 instances"

    instances = filter_instances(project)

    for i in instances:
        print("Stopping {0}...".format(i.id))
        # 対象 instance を停止
        i.stop()

    return



# 直接呼び出された場合のみ、続く処理を実行
if __name__ == '__main__':
    # グループ化したファンクションをコール
    instances()
