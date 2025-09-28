# this subroutine is renaming the files
$doneDir = ".\done" # Define the name of the subdirectory

# Create the 'done' directory if it doesn't exist
# Uses "-ErrorAction SilentlyContinue" to suppress error if it already exists
if (-not (Test-Path -Path $doneDir -PathType Container)) {
    Write-Host "Creating directory: $doneDir"
    New-Item -Path $doneDir -ItemType Directory -ErrorAction SilentlyContinue | Out-Null
}

Get-ChildItem -File | ForEach-Object {
    # Construct the new name (filename only)
    $newName = $_.Name.Substring(0, 46) + '.pdf'

    # --- Step 1: Rename the file in the current directory ---
    # NOTE: Add error handling here if needed in your actual use case
    Rename-Item -Path $_.FullName -NewName $newName 

    # --- Step 2: Move the *renamed* file to the 'done' directory ---
    # This assumes Rename-Item succeeded. We target the $newName in the current directory.
   
    Move-Item -Path $newName -Destination $doneDir 
}

Write-Host "Processing loop finished."
