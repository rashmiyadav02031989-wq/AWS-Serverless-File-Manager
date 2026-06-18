import json
import boto3

s3 = boto3.client("s3")

BUCKET = "Your Bucket Name"

def lambda_handler(event, context):

    try:
        # Optional: filter by folder (prefix)
        params = event.get("queryStringParameters") or {}
        #key = f"upload/{uuid.uuid4()}-{file_name}"
        prefix = params.get("prefix", "upload/")
        print("list prefix =", prefix)
        response = s3.list_objects_v2(
            Bucket=BUCKET,
            Prefix=prefix
        )

        files = []
        for obj in response.get("Contents", []):
            key = obj["Key"]

            if key == "upload/":
                continue

        # ✅ Generate GET URL
            url = s3.generate_presigned_url("get_object",
            Params={
                "Bucket": BUCKET,
                "Key": key
                  },
            ExpiresIn=600
            )

            files.append({
            "key": key,
            "url": url,  # 👈 IMPORTANT
            "size": obj["Size"],
            "lastModified": obj["LastModified"].isoformat()
            })


        
        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET,POST,OPTIONS",
                "Access-Control-Allow-Headers": "*"
            },
            "body": json.dumps(files)
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
