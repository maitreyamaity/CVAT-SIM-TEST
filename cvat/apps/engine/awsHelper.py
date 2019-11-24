import boto3

class AWSHelper:
    def __init__(self):
        self.client = boto3.client(
            's3', 
            aws_access_key_id='XXXXXXXXXXXXXXXXXXXXX', 
            aws_secret_access_key='XXXXXXXXXXXXXXXXXXXXXXXX',
            )
        self.BUCKET_NAME = 'XXXXXXXXXXXXXXXXXXXXXX'
        
    def uploadFile(self, filePath, fileKey):
        try:
            with open(filePath, "rb") as f:
                self.client.upload_fileobj(f, self.BUCKET_NAME, fileKey)
            f.close()
        except Exception as e:
            print('AWS File Upload Error:',e)
    
    def presignedUrl(self, fkey):
        try:
            response = self.client.generate_presigned_url('get_object', Params={'Bucket': self.BUCKET_NAME, 'Key': fkey}, ExpiresIn=3600, HttpMethod='GET')
        except Exception as e:
            print('AWS Url Create Error:',e)
            return None
        return response