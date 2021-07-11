def upload_df_s3(df, path):
    """
    This function uploads files directly from Python to S3 before checking duplicates
    Input
    df - pandas dataframe
    path - S3 file path (s3://<bucket-name>/<file-name>.csv)
    """
    import boto3
    s3 = boto3.resource('s3')
    
    bucket_name = path.split('://')[1].split('/')[0]
    file_name = path.replace('s3://'+bucket_name+'/', '')
    
    my_bucket = s3.Bucket(bucket_name)
    
    for file in my_bucket.objects.all():
        print('Checking if file with same name is already present in S3.\n')
        if file_name in file.key:
            print('File name \"{}\" already present. Please try with a different name'.format(file_name))
            break
        else:
            print('Uploading the file to S3 at - {}'.format(path))
            df.to_csv(path, index=0)
            break
