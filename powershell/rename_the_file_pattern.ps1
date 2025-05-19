<#
.SYNOPSIS
Renames files in the current directory based on a specific pattern.
It replaces the part of the filename before the last underscore with a fixed prefix,
while keeping the part after the previous underscore.

.DESCRIPTION
This script iterates through files in the current directory. For each file, it finds
the last underscore in the filename. If found, it constructs a new filename consisting
of the predefined prefix "SH ID_ Title_SH Controller Date_" followed by the original
part of the filename that came after the last underscore. It then renames the file.
Files without an underscore or ending in an underscore are skipped.

#>

# --- Configuration ---
# Define the new prefix string that will replace the part before the last underscore
$newPrefix = "SH ID_ Title_SH Controller Date_"
# --- End Configuration ---

Write-Host "Starting file rename process..."
Write-Host "New prefix: '$newPrefix'"
Write-Host "Scanning files in the current directory: '$($PWD.Path)'"
Write-Host "------------------------------------"

# Get all files in the current directory
Get-ChildItem -File | ForEach-Object {
    # Store current file's details
    $originalFileObject = $_
    $originalName = $originalFileObject.Name
    $originalFullName = $originalFileObject.FullName

    # Find the index of the *last* underscore in the filename
    $lastUnderscoreIndex = $originalName.LastIndexOf('_')

    # Proceed only if an underscore was found and it's not the very last character
    if ($lastUnderscoreIndex -ge 0 -and $lastUnderscoreIndex -lt ($originalName.Length - 1)) {
        try {
            # Extract the part of the filename *after* the last underscore
            $suffixPart = $originalName.Substring($lastUnderscoreIndex + 1)

            # Construct the new filename
            $newName = $newPrefix + $suffixPart

            # --- Rename the file ---
            # Use -Verbose to see which files are being targeted
            # !! IMPORTANT: Use -WhatIf for testing !! Remove it to perform actual renaming.
            Write-Verbose "Planning to rename '$originalName' to '$newName'" -Verbose
            Rename-Item -Path $originalFullName -NewName $newName -ErrorAction Stop 

        } catch {
            # Catch any errors during substring or renaming for this specific file
            Write-Error "Could not process file '$originalName'. Error: $($_.Exception.Message)"
        }
    } else {
        # Skip files that don't contain an underscore or end with one
        Write-Verbose "Skipping file '$originalName': No underscore found, or it's the last character." -Verbose
    }
}

Write-Host "------------------------------------"
Write-Host "Script finished."


