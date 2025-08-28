# assign the increment
$i = 1
$doneDir = ".\done" # Define the name of the subdirectory

# Create the 'done' directory if it doesn't exist
# Uses -ErrorAction SilentlyContinue to suppress error if it already exists
if (-not (Test-Path -Path $doneDir -PathType Container)) {
    Write-Host "Creating directory: $doneDir"
    New-Item -Path $doneDir -ItemType Directory -ErrorAction SilentlyContinue | Out-Null
}

Get-ChildItem -File | ForEach-Object {
    # Construct the new name (filename only)
    $newName = $_.Name.Substring(0, 6) + ('{0:D4}' -f $i++) + $_.Name.Substring(10)

    # --- Step 1: Rename the file in the current directory ---
    # NOTE: Add error handling here if needed in your actual use case
    Rename-Item -Path $_.FullName -NewName $newName -WhatIf

    # --- Step 2: Move the *renamed* file to the 'done' directory ---
    # This assumes Rename-Item succeeded. We target the $newName in the current directory.
    # CAVEAT with -WhatIf: Since Rename-Item -WhatIf doesn't *actually* rename,
    # the file named $newName won't exist yet. The 'What if' for Move-Item
    # The code below may display an error or target a non-existent file during simulation.
    # Test by removing -WhatIf from Rename-Item first OR remove both to run for real.
    Move-Item -Path $newName -Destination $doneDir -WhatIf
}

Write-Host "Processing loop finished. Next available number: $i"
