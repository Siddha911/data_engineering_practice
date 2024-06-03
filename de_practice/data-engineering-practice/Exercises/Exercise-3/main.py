import boto3


def main(bucket: str, key: str):

    s3 = boto3.client('s3')
    content = s3.get_object(Bucket=bucket, Key=key)['Body'].read().decode('utf-8')


if __name__ == "__main__":
    main(bucket='commoncrawl', key='crawl-data/CC-MAIN-2022-05/wet.paths.gz')
