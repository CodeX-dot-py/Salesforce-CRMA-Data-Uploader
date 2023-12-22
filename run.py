from sf_analytics_file_uploader import UploadToSfOrg

# Initialize the uploader
uploader = UploadToSfOrg(username='your_username',
                        password='your_password',
                        security_token='your_security_token')

# Example usage
result = uploader.write_to_crma_app(crma_app_alias='your_crma_app_alias',
                                     dataset_alias='your_dataset_alias',
                                     local_dataset_path='path/to/your/local/dataset.csv',
                                     local_dataset_metadata_path='path/to/your/local/dataset_metadata.json',
                                     data_operation_type='Append')