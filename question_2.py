#Code an AWS Lambda function to store a document or PDF file in an S3 bucket.?


import json
import boto3
import base64
import uuid
from io import BytesIO

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    try:
        file_data = event.get('file_data') 
        bucket_name = event.get('bucket_name') 
        file_name = event.get('file_name', f"{str(uuid.uuid4())}.pdf")  
        
        if not file_data or not bucket_name:
            return {
                'statusCode': 400,
                'body': json.dumps('Missing required parameters: file_data or bucket_name.')
            }

        file_content = base64.b64decode(file_data)

        s3_client.put_object(
            Bucket=bucket_name,
            Key=file_name,
            Body=file_content,
            ContentType='application/pdf'  # Assuming it's a PDF
        )

        return {
            'statusCode': 200,
            'body': json.dumps(f"File uploaded successfully to {bucket_name}/{file_name}")
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error uploading file: {str(e)}")
        }
