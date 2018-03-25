# aws-backup
Automate taking AMI backup with python and Lambda

## About

This project is a demo, and uses boto3 to manage AWS EC2 instance AMI backup.

## Confuguring

backup_ami uses the confuguration file created by the AWS cli. e.g.

`aws configure --profile backup_user`

## Running

`pipenv run "python backup_ami\backup_ami.py"`
