
def upload_file(s3,file_name, bucket):
    """
    Function to upload a file to an S3 bucket
    """
    object_name = file_name
    response = s3.upload_file(file_name, bucket, object_name)

    return response


def download_file(s3, file_name, bucket):
    """
    Function to download a given file from an S3 bucket
    """
    obj = s3.get_object(Bucket=BUCKET, Key=filename)
    output = obj['Body'].read()
    response = make_response(output)
    response.mimetype = mimetypes.MimeTypes().guess_type(filename)[0]

    return response


def list_files(s3, bucket):
    """
    Function to list files in a given S3 bucket
    """
    contents = []
    signed_url = {}
    try:
        for item in s3.list_objects(Bucket=bucket)['Contents']:
            object_key = item['Key']
            response = s3.generate_presigned_url('get_object',
                                                    Params={'Bucket': bucket,
                                                            'Key': object_key},
                                                    ExpiresIn=3600)
            signed_url = {'url': response, 'name': object_key}
            #signed_url.update(signed_url)
            #print(response)
            contents.append(signed_url)
            
    except Exception as e:
        pass
    return contents
