import boto3

# 直接呼び出された場合のみ、続く処理を実行
if __name__ == '__main__':
    session = boto3.Session(profile_name='backupuser')
    ec2 = session.resource("ec2")

    for i in ec2.instances.all():
        print(i)
