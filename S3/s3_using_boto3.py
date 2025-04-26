import boto3

# Initialize S3 client
s3 = boto3.client('s3')

# Bucket name (must be globally unique)
bucket_name = 'pavankabucketboto3'

# Region (change if needed)
region = 'us-east-1'

# Create the bucket
if region == 'us-east-1':
    s3.create_bucket(Bucket=bucket_name)
else:
    s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={'LocationConstraint': region}
    )

print(f"S3 Bucket '{bucket_name}' created successfully.")
