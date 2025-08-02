from fastapi import FastAPI, HTTPException
import os
import uuid

from bills.clients.aws import AWSBillingClient
from bills.parser.report import ReportParser
from bills.parser.formatter import CABFormatter

app = FastAPI()

# Config
BUCKET = os.getenv('BUCKET')
PREFIX = os.getenv('PREFIX')
ROOT_DIR = os.path.join(os.getcwd(), 'files')

@app.get("/billing-report/aws")
def get_aws_report():
    client = AWSBillingClient(bucket_name=BUCKET, prefix=PREFIX)
    # parser = ReportParser()
    # formatter = CABFormatter()

    parquets = client.list_reports()
    if not parquets:
        raise HTTPException(status_code=404, detail="No reports found.")

    for parquet in parquets[:1]:
        local_csv = os.path.join(ROOT_DIR, f"{uuid.uuid4()}")
        client.download_report(parquet, local_csv)


@app.get("/billing-report/gcp")
def get_gcp_report():
    client = GCPBillingClient(...)  # same interface
