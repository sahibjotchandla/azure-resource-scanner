This project is a simple Azure SDK–based tool that authenticates to Azure and lists:
- All resource groups with their locations
- All resources in the subscription with their type and tags

The goal is to demonstrate basic Azure authentication, ARM usage, and SDK interaction using Python.

--------------------------------------------------

Prerequisites

- Python 3.10+
- Azure CLI installed
- An Azure subscription
- Logged in via Azure CLI

--------------------------------------------------

Setup

1. Clone the repository

   git clone https://github.com/<your-username>/azure-resource-scanner.git
   cd azure-resource-scanner

2. Create and activate a virtual environment

   python -m venv .venv

   PowerShell:
   .venv\Scripts\Activate.ps1

3. Install dependencies

   pip install -r requirements.txt

4. Login to Azure

   az login

--------------------------------------------------

Running the Script

1. Get your subscription ID

   az account show --query id -o tsv

2. Set the environment variable

   PowerShell:
   $env:AZURE_SUBSCRIPTION_ID="your-subscription-id"

3. Run the scanner

   python scanner.py

--------------------------------------------------

Example Output

See the screenshot below for an example of the script output, including:
- Resource group names and locations
- Resource names, types, and tags

docs/output.png

--------------------------------------------------

Technologies Used

- Python
- Azure SDK for Python
- Azure Identity
- Azure Resource Manager (ARM)
- Azure CLI

--------------------------------------------------

Notes

- Authentication is handled using DefaultAzureCredential, which reuses Azure CLI login
- No secrets or credentials are stored in code
