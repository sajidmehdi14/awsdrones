import boto3
session = boto3.Session()
import boto3
session = boto3.Session(profile_name='default')
as_client = session.client('autoscaling')
as_client.describe_auto_scaling_groups()
as_client.describe_policies()
as_client.execute_policy(AutoScalingGroupName='alertdrone-asg', PolicyNmae='scale down')
as_client.execute_policy(AutoScalingGroupName='alertdrone-asg', PolicyName='scale down')
