Certainly! Here's the complete README.md content in markdown:

```markdown
# Salesforce Analytic Data Uploader

The Salesforce Analytic Data Uploader is a Python package designed to simplify the process of uploading analytical data to Salesforce. It provides a set of tools for interacting with the Salesforce SOAP API, making it easier for developers to integrate data uploads into their Salesforce workflows.

## 📚 Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Features](#features)
4. [Configuration](#configuration)
5. [Contributing](#contributing)
6. [License](#license)

## 🚀 Installation

Get started with the `sf_analytic_data_uploader` package in a breeze using pip:

```bash
pip install sf_analytic_data_uploader
```

### Supported Python Versions

The package is compatible with Python 3.6 and above.

## 💡 Usage

### Authentication
To use the package, you need to authenticate with your Salesforce instance. Follow these steps:

1. Provide your Salesforce username, password, and security token to the package.
2. Initiate the authentication process using the `Login` class.

Example:

```python
from sf_analytic_data_uploader import Login

username = "your_salesforce_username"
password = "your_salesforce_password"
security_token = "your_security_token"

# Initialize the Login class
login_instance = Login(username, password, security_token)

# Retrieve session ID and server URL
session_id = login_instance.get_session_id()
server_url = login_instance.get_server_url()
```

### Uploading Data
Learn how to upload both data and metadata to Salesforce using the package. Follow these steps:

1. Create an instance of the `UploadToSfOrg` class.
2. Use the provided methods to upload data and metadata.

Example:

```python
from sf_analytic_data_uploader import UploadToSfOrg

# Provide Salesforce credentials
username = "your_salesforce_username"
password = "your_salesforce_password"
security_token = "your_security_token"

# Initialize the UploadToSfOrg class
uploader = UploadToSfOrg(username, password, security_token)

# Perform data upload operations
uploader.write_to_crma_app(
    crma_app_alias="your_crma_app_alias",
    dataset_alias="your_dataset_alias",
    local_dataset_path="path/to/local/dataset.csv",
    local_dataset_metadata_path="path/to/local/metadata.json",
    data_operation_type="upload_type"
)
```

## 🌟 Features

- **Authentication**: Easily authenticate with your Salesforce instance using the provided `Login` class.
- **Data Upload**: Use the `UploadToSfOrg` class to upload both data and metadata to Salesforce.
- **SOAP API Integration**: Interact with the Salesforce SOAP API for seamless data communication.

## ⚙️ Configuration

Configure the package with your Salesforce credentials and customize data upload operations. Refer to the [Usage](#usage) section for detailed examples.

## 🤝 Contributing

If you find any issues or have suggestions for improvement, feel free to open an [issue](https://github.com/your_username/sf_analytic_data_uploader/issues) or submit a [pull request](https://github.com/your_username/sf_analytic_data_uploader/pulls). Contributions are welcome!

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

Please replace placeholders such as `your_salesforce_username`, `your_salesforce_password`, `your_security_token`, `path/to/local/dataset.csv`, `path/to/local/metadata.json`, `your_crma_app_alias`, `your_dataset_alias`, and others with your actual values and paths.