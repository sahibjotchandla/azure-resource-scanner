import os
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient

def main():
    subscription_id = os.environ.get("AZURE_SUBSCRIPTION_ID")
    if not subscription_id:
        raise SystemExit(
            "Missing AZURE_SUBSCRIPTION_ID. Set it like:\n"
            "  (PowerShell)  $env:AZURE_SUBSCRIPTION_ID = \"<sub-id>\"\n"
            "  (bash/zsh)    export AZURE_SUBSCRIPTION_ID=\"<sub-id>\""
        )

    credential = DefaultAzureCredential(exclude_interactive_browser_credential=False)
    client = ResourceManagementClient(credential, subscription_id)

    # List resource groups + locations
    print("\n=== Resource Groups ===")
    rgs = list(client.resource_groups.list())
    if not rgs:
        print("(none)")
    for rg in rgs:
        print(f"- {rg.name}  | location={rg.location}")

    # List resources with type + tags
    print("\n=== Resources (type + tags) ===")
    resources = list(client.resources.list())
    if not resources:
        print("(none)")
    for r in resources:
        tags = r.tags or {}
        print(f"- {r.name}")
        print(f"  id:   {r.id}")
        print(f"  type: {r.type}")
        print(f"  rg:   {r.id.split('/resourceGroups/')[1].split('/')[0] if r.id else 'unknown'}")
        print(f"  tags: {tags}\n")

if __name__ == "__main__":
    main()
