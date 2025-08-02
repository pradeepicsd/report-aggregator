import boto3
import os
import pandas as pd
from .base import BaseProviderClient

class AWSBillingClient(BaseProviderClient):
    def __init__(self, bucket_name: str, prefix: str, region: str = "us-east-1", profile_name: str = 'profile'):
        self.bucket_name = bucket_name
        self.prefix = prefix
        self.region = region
        session = boto3.Session(profile_name=profile_name, region_name=region)
        # self.s3 = boto3.client("s3", region_name=region)
        self.s3 = session.client("s3")

    def list_reports(self):
        response = self.s3.list_objects_v2(Bucket=self.bucket_name)
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            return [
                obj["Key"]
                for obj in response.get("Contents", [])
                if obj["Key"].endswith(".parquet")
            ]
        return []

    def list_buckets(self):
        return self.s3.list_buckets()

    def download_report(self, key: str, dest_path: str):
        with open(f"{dest_path}.parquet", "wb") as f:
            self.s3.download_fileobj(self.bucket_name, key, f)
        df = pd.read_parquet(f"{dest_path}.parquet")
        df.to_csv(f"{dest_path}.csv")
        return dest_path
