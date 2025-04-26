import boto3

# Initialize EC2 client
ec2 = boto3.client('ec2', region_name='us-east-1')  # change region if needed

# Launch EC2 instance
response = ec2.run_instances(
    ImageId='ami-065aeacd44e98d9ac',  # Amazon Linux 2 AMI (N. Virginia)
    InstanceType='t2.micro',
    KeyName='pavan_bl',  # Your  key pair name
    MinCount=1,
    MaxCount=1,
    SecurityGroupIds=['sg-0b46fe866e95164bd'],  #  your actual SG ID
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {'Key': 'Name', 'Value': 'ec2usingboto3'}
            ]
        }
    ]
)

# Print instance ID
instance_id = response['Instances'][0]['InstanceId']
print(f"EC2 Instance launched with ID: {instance_id}")
