# Azure Resource Scanner

Lightweight Python-based utility that authenticates to Azure and enumerates
resource groups and resources within a subscription using Azure SDKs.

Designed to demonstrate Azure authentication, ARM interaction, and basic
cloud inventory automation.

> ⚠️ All subscription IDs and resource IDs shown in this repository are
partially redacted. Replace them with your own values when running locally.

---

## 🧱 Architecture Overview

**Language:** Python 3

**Authentication:**
- Azure CLI (`az login`)
- Azure Identity (`DefaultAzureCredential`)

**Azure APIs Used:**
- Azure Resource Manager (ARM)

**SDKs:**
- `azure-identity`
- `azure-mgmt-resource`

**Scope:**
- Single Azure subscription
- Read-only resource enumeration

---

## 📂 Repository Layout

```text
scanner.py              # Main script to scan Azure resources
requirements.txt        # Python dependencies
README.md               # Project documentation
.gitignore              # Git ignore rules

docs/
  output.png            # Example terminal output (redacted)
