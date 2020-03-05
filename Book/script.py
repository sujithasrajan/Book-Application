import boto3
#USED TO CREATE INSTANCE FROM THE IMAGE ID AND SHOW DETAILS ABOUT THE INSTANCE
ec2 = boto3.client('ec2')
ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
ec2.run_instances(ImageId='ami-077580c5d12f8f427', MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName='ec2')
response = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
print(response)
MyPublicDnsName = response['Reservations'][0]['Instances'][0]['PublicDnsName']
print(MyPublicDnsName)
MyInstanceId = response['Reservations'][0]['Instances'][0]['InstanceId']
print(MyInstanceId)


#USED TO START THE RDS AND GET THE ENDPOINT OF THE RDS
rds = boto3.client('rds')
response = rds.describe_db_instances(DBInstanceIdentifier = 'sujitha')
print(response)
rds.start_db_instance(DBInstanceIdentifier = 'sujitha’)
response = rds.describe_db_instances(DBInstanceIdentifier = 'sujitha')
print(response)
MyRdsAddress = response['DBInstances'][0]['Endpoint']['Address']

#LOAD BALANCER 
elb = boto3.client('elbv2')
response = elb.create_target_group(Name='TG1', Protocol='HTTP', Port=80, VpcId='vpc-f60f0e9e', TargetType='instance')
print(response)
MyTG = response['TargetGroups'][0]
print(MyTG)
response = elb.register_targets(TargetGroupArn='arn:aws:elasticloadbalancing:us-east-2:318865060263:targetgroup/TG1/640aed97a010e997', Targets=[{'Id': 'ami-077580c5d12f8f427'}, {'Id': 'MyInstanceId'}])
response = elb.create_load_balancer(Name='MyLBName',Subnets=[MySubnets[0]['SubnetId'], MySubnets[1]['SubnetId'], MySubnets[2]['SubnetId']])
MyLB = response['LoadBalancers'][0]
print(MyLB)
response = elb.create_listener(LoadBalancerArn='arn:aws:elasticloadbalancing:us-east-2:318865060263:targetgroup/TG1/640aed97a010e997', Protocol='HTTP', Port=80, DefaultActions=[{'Type': 'forward', 'TargetGroupArn': MyTG['TargetGroupArn']}])

#AUTOSCALING WORKS
atc = boto3.client('autoscaling')
response = atc.create_launch_configuration(LaunchConfigurationName='FINALlc', ImageId = 'ami-077580c5d12f8f427', InstanceType='t2.micro', KeyName='ec2')
response = atc.create_auto_scaling_group(AutoScalingGroupName = 'FINALas', LaunchConfigurationName='FINALlc', MinSize = 1, MaxSize = 2, DesiredCapacity = 1, AvailabilityZones = ['us-east-2a','us-east-2b','us-east-2c'], TargetGroupARNs=['arn:aws:elasticloadbalancing:us-east-2:318865060263:targetgroup/TG1/640aed97a010e997'])
