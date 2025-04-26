import boto3

# Initialize S3 client
s3 = boto3.client('s3')

# List buckets
response = s3.list_buckets()

# Print bucket names
print("Your S3 Buckets:")
for bucket in response['Buckets']:
    print(f" - {bucket['Name']}")
