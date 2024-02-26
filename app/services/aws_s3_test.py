import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError
from dotenv import load_dotenv
from os import environ as env

load_dotenv()

# Configure your S3 bucket details
S3_BUCKET = env.get("S3_BUCKET")
S3_KEY = env.get("S3_KEY")
S3_SECRET = env.get("S3_SECRET")

print(S3_KEY)

# Initialize a session using Amazon S3
s3 = boto3.client(
    "s3",
    aws_access_key_id=S3_KEY,
    aws_secret_access_key=S3_SECRET,
)


# Function to test the credentials by listing the buckets
def test_s3_credentials():
    try:
        # Attempt to list buckets
        response = s3.list_buckets()
        # If successful, return the list of bucket names
        buckets = [bucket["Name"] for bucket in response["Buckets"]]
        return True, buckets
    except NoCredentialsError:
        return False, "No credentials could be found"
    except PartialCredentialsError:
        return False, "Incomplete credentials"
    except ClientError as e:
        # Handling specific error messages from AWS
        if e.response["Error"]["Code"] == "InvalidAccessKeyId":
            return False, "Invalid Access Key ID"
        elif e.response["Error"]["Code"] == "SignatureDoesNotMatch":
            return (
                False,
                "The request signature we calculated does not match the signature you provided",
            )
        else:
            return False, f"Client Error: {e.response['Error']['Message']}"


# Run the test and print results
success, result = test_s3_credentials()
if success:
    print("Success! Here are your buckets:")
    for bucket in result:
        print(f"- {bucket}")
else:
    print(f"Failed to verify credentials: {result}")
