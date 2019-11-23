import boto3
import botocore
import os

class AWSHelper:
    def __init__(self):
        self.client = boto3.client(
            's3',
            aws_access_key_id="AKIAQESGBNJZKR6ZHXL2",
            aws_secret_access_key="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",
        )
        self.BUCKET_NAME = "adv-tec.test-bucket"

    def serchContent(self, fname):
        fname = fname + '/'
        paginator = self.client.get_paginator('list_objects')
        page_iterator = paginator.paginate(Bucket=self.BUCKET_NAME)
        for page in page_iterator:
            contents = page['Contents']
            for obj in contents:
                key = obj["Key"]
                if key == fname:
                    return True

        return False

    def createFolder(self, directory_name):
        # directory_name = "maitreya/jap" #it's name of your folders
        self.client.put_object(Bucket=self.BUCKET_NAME, Key=(directory_name + '/'))

    def uploadFile(self, filepath, directory_name):
        file_name = os.path.basename(filepath)
        with open(filepath, "rb") as f:
            self.client.upload_fileobj(f, self.BUCKET_NAME, '%s/%s' % (directory_name, file_name))
        f.close()

    def downloadFile(self, fileKey, output_path):
        try:
            self.client.download_file(self.BUCKET_NAME, fileKey, output_path)
        except botocore.exceptions.ClientError as e:
            print(e)

