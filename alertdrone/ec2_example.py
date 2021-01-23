# coding: utf-8
import boto3
session = boto3.Session(profile_name='boto3dev')
ec2 = session.resource('ec2')
key_name = 'drone_key'
key_path = key_name + '.pem'
key = ec2.create_key_pair(KeyName=key_name)
key.key_material
with open(key_path, 'w') as key_file:
    key_file.write(key.key_material)
    
get_ipython().run_line_magic('ls', '-al')
get_ipython().run_line_magic('ls', '-altr')
import os, stat
os.chmod(key_path, stat.S_IRUSR | stat.S_IWUSR)
get_ipython().run_line_magic('ls', '-altr')
ec2.images.filter(Owners=['amazon'])
list(ec2.images.filter(Owners=['amazon']))
img  = ec2.Image('ami-0323c3dd2da7fb37d')
img.name
ec2_apse2 = session.resource('ec2', region_name='ap-southeast-2')
img_apse2  = ec2_apse2.Image('ami-0323c3dd2da7fb37d')
img_apse2.name
img.name
ami_name = 'amzn2-ami-hvm-2.0.20200406.0-x86_64-gp2'
filters = [{'Name': 'name', 'Values': [ami_name]}]
list(ec2.images.filter(Owners=['amazon'], Filtes=filters))
list(ec2.images.filter(Owners=['amazon'], Filters=filters))
list(ec2_apse2.images.filter(Owners=['amazon'], Filters=filters))
img
key
get_ipython().run_line_magic('ls', '')
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key.key_name)
instances
ec2.Instance(id='i-0429d6bc748df7e95')
inst = instances[0]
inst
inst.terminate()
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key.key_name)
inst = instances[0]
inst.public_dns_name
inst.public_dns_name
inst.wait_until_running()
inst.public_dns_name
inst.reload()
inst.public_dns_name
inst.security_groups
sg = ec2.SecurityGroup(inst.security_groups[0]['GroupId'])
sg.authorize_ingress
sg.authorize_ingress(IpPermissions=[{'FromPort': 22, 'ToPort': 22, 'IpProtocol': 'TCP', 'IpRanges': [{'CidrIp': '119.160.99.84/32'}]}])
inst.security_groups
sg.authorize_ingress(IpPermissions=[{'FromPort': 80, 'ToPort': 80, 'IpProtocol': 'TCP', 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}])
sg.authorize_ingress(IpPermissions=[{'FromPort': 80, 'ToPort': 80, 'IpProtocol': 'TCP', 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}])
get_ipython().run_line_magic('history', '')
