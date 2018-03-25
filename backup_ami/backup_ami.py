import boto3
import click

session = boto3.Session(profile_name='backupuser')
ec2 = session.resource("ec2")

@click.command()
@click.option('--project', default=None,
              help="Only instances for project (tag Project:<name>)")
def list_instances(project):
    # Doc string
    "List EC2 instances"
    instances = []

    if project:
        filters = [{'Name': 'tag:Project', 'Values':[project]}]
        instances = ec2.instances.filter(Filters=filters)
    else:
        instances = ec2.instances.all()

    for i in instances:
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

# 直接呼び出された場合のみ、続く処理を実行
if __name__ == '__main__':
    list_instances()
