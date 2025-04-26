import boto3

# Initialize S3 client
s3 = boto3.client('s3')

# File and bucket details
file_path = "D:/major research paper/research paper ieee major.docx"  # Local file path
bucket_name = 'pavankabucketboto3'                 # Replace with your bucket
object_name = 'major_research_paper.txt'              # Name to save in S3

# Upload file
s3.upload_file(file_path, bucket_name, object_name)

print(f"'{file_path}' uploaded to S3 bucket '{bucket_name}' as '{object_name}'.")
