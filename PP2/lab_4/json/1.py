import json

# Try to load JSON data from file
try:
    with open("sample-data.json", "r") as file:
        data = json.load(file)  # Load the JSON data
except FileNotFoundError:
    print("Error: The file 'sample-data.json' was not found.")
    exit()

# Extract the list of interfaces
interfaces = data.get("imdata", [])

# Print table header
print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<10} {'MTU':<10}")
print("-" * 80)

# Loop through each interface and extract required details
for interface in interfaces:
    attributes = interface.get("l1PhysIf", {}).get("attributes", {})  # Safely get attributes

    # Extract required fields with default values in case they're missing
    dn = attributes.get("dn", "N/A")
    description = attributes.get("descr", "")  # Empty if not present
    speed = attributes.get("speed", "N/A")
    mtu = attributes.get("mtu", "N/A")

    # Print formatted output
    print(f"{dn:<50} {description:<20} {speed:<10} {mtu:<10}")
