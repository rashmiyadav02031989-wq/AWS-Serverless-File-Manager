import json
import boto3
import urllib.parse

s3 = boto3.client("s3")
BUCKET = "Your-S3-Bucket-Name"

def lambda_handler(event, context):

    params = event.get("queryStringParameters") or {}
    key = params.get("key")

    if not key:
        return {
            "statusCode": 400,
            "headers": {"Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"error": "Missing key"})
        }

    try:
        # decode key (important)
        key = urllib.parse.unquote(key)

        s3.delete_object(
            Bucket=BUCKET,
            Key=key
        )

        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({"message": "Deleted successfully"})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({"error": str(e)})
        }
