import boto3
import click

session = boto3.Session(profile_name='backupuser')
ec2 = session.resource("ec2")

@click.command()
def list_instances():
    # Doc string
    "List EC2 instances"
    for i in ec2.instances.all():
        print(', '.join((
            i.id,
            i.instance_type,
            i.placement['AvailabilityZone'],
            i.state['Name'],
            i.public_dns_name,
            i.image_id)))

    return

# 直接呼び出された場合のみ、続く処理を実行
if __name__ == '__main__':
    list_instances()
