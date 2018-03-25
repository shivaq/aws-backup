▼ 使用準備
-------------------------------------------------
boto3 をインポート
# import boto3

特定の"AWS Access Key ID " に紐付いた Provile_name で、セッションを取得
# session = boto3.Session(profile_name='backupuser')
ec2 のサービスを取得
# ec2 = session.resource("ec2")
(紐付いた AWS アカウントの)ec2 の 全インスタンス情報を取得
# inst = ec2.instances.all()

試しに ec2 インスタンスのリストから一つ変数に格納してみる
# i = list(inst)[0]

AZ や グループ名などの情報
# i.placement

EC2 インスタンスの状態
            i.id,
            i.instance_type,
            i.placement['AvailabilityZone'],
            i.state['Name'],
            i.public_dns_name,
            i.image_id)))
