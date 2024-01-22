#!/bin/bash

REQUIREMENTS_FILE="requirements.txt"
TEMP_REQUIREMENTS_FILE="temp_requirements.txt"

# Check if requirements.txt file exists
if [ ! -f "$REQUIREMENTS_FILE" ]; then
    # If not, create it using pip freeze
    pip freeze > "$REQUIREMENTS_FILE"
    echo "Created $REQUIREMENTS_FILE using pip freeze."
fi

# Ensure the while loop reads the last line by setting the input file descriptor to the end of the file
exec 3<"$REQUIREMENTS_FILE"

while IFS= read -r LINE <&3 || [ -n "$LINE" ]; do
    # Skip empty lines or lines starting with '#' (comments)
    if [[ -z "$LINE" || "$LINE" == "#"* ]]; then
        continue
    fi

    # Check if the line contains '=='
    if [[ "$LINE" == *"=="* ]]; then
        # If '==' is present, keep the line unchanged
        echo "$LINE" >> "$TEMP_REQUIREMENTS_FILE"
    else
        PACKAGE_NAME="$LINE"
        
        # Use pip list to get the installed version of the package
        INSTALLED_VERSION=$(pip list --format=freeze | grep "^$PACKAGE_NAME==" | awk -F '==' '{print $2}')

        # Check if the package version is not empty
        if [ -n "$INSTALLED_VERSION" ]; then
            # Append the package name and version to a temporary file
            echo "$PACKAGE_NAME==$INSTALLED_VERSION" >> "$TEMP_REQUIREMENTS_FILE"
        else
            echo "Warning: Unable to determine the version of $PACKAGE_NAME. Skipping."
        fi
    fi
done

# Close the file descriptor
exec 3<&-

# Replace the original requirements file with the temporary file
mv "$TEMP_REQUIREMENTS_FILE" "$REQUIREMENTS_FILE"

echo "Updated $REQUIREMENTS_FILE with package versions."


#This code basically appends version to package if not present in requirements.txt.
