import boto3

# Initialize S3 client
s3 = boto3.client('s3')

# Details of the object to delete
bucket_name = 'pavankabucketboto3'       # Replace with your bucket name
object_name = 'major_research_paper.txt'    # Replace with your file name in S3

# Delete the object
response = s3.delete_object(Bucket=bucket_name, Key=object_name)

print(f"Deleted '{object_name}' from bucket '{bucket_name}'")
