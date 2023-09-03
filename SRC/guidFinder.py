import re

# Path to the csproj file
csproj_path = 'application.csproj'

# Read the content of the csproj file
with open(csproj_path, 'r') as file:
    csproj_content = file.read()

# Find and replace GUID content with uppercase versions
def upper_guid_content(match):
    return match.group(0).upper()

# Search for GUIDs in the csproj content using a regular expression
guid_pattern = r'(?<=<ProjectGuid>){.*?}(?=<\/ProjectGuid>)'
guids_found = re.findall(guid_pattern, csproj_content, re.DOTALL)

if not guids_found:
    print("Error: No GUID found in the csproj file.")
else:
    # Replace the GUID content with uppercase versions
    patched_content = re.sub(guid_pattern, upper_guid_content, csproj_content, flags=re.DOTALL)

    # Write the patched content back to the file
    with open(csproj_path, 'w') as file:
        file.write(patched_content)

    print("GUID content within <ProjectGuid> tags have been patched to uppercase.")
