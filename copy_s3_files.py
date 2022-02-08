def copy_s3_files(source_dict, destination_dict):
    """
    This function copies file from one S3 location/folder and saves it to another
    """
    import boto3
    s3 = boto3.resource('s3')

    source_folder_name = source_dict.get('source_folder_name')
    source_bucket_name = source_dict.get('source_bucket_name')
    source_bucket = s3.Bucket(source_bucket_name)

    destination_folder_name = destination_dict.get('destination_folder_name')
    destination_bucket_name = destination_dict.get('destination_bucket_name')
    destination_bucket = s3.Bucket(destination_bucket_name)

    count = 0
    overall_count = 0
    for file in source_bucket.objects.all():
        overall_count += 1
        if source_folder_name in file.key:
            count += 1
            print(file.key)

            copy_source = {'Bucket': source_bucket_name, 'Key': file.key}
            new_key = file.key.replace(source_folder_name, destination_folder_name)
            print(new_key)

            destination_bucket.copy(copy_source, new_key)
    print('Total objects traversed -> {}.\nTotal objects copied -> {}'.format(overall_count, count))

source_dict = {'source_bucket_name': 'mybucket123',
               'source_folder_name': 'myfolder123'}

destination_dict = {'destination_bucket_name': 'mybucket789',
                    'destination_folder_name': 'myfolder789'}

copy_s3_files(source_dict, destination_dict)
