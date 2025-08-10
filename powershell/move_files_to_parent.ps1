# Specify the parent directory
$parentFolder = "main"

# Get all subdirectories within the parent folder that start with "ID"
$subFolders = Get-ChildItem -Path $parentFolder -Directory | Where-Object {$_.Name -like "ID*"}

# Loop through each subdirectory
foreach ($subFolder in $subFolders) {
    # Get all files within the current subdirectory
    $files = Get-ChildItem -Path $subFolder.FullName -File

    # Loop through each file and move it to the parent directory
    foreach ($file in $files) {
        try {
            Move-Item -Path $file.FullName -Destination $parentFolder -Force
            Write-Host "Moved '$($file.Name)' from '$($subFolder.Name)' to '$parentFolder'"
        } catch {
            Write-Warning "Error moving '$($file.Name)': $($_.Exception.Message)"
        }
    }
}

Write-Host "Finished moving files."

# HERE's THE VERSION THAT IGNORES THE FILE NAMES, just moved them all into a single directory
# It is useful for cases when you want to get rid of a bunch of folders, like from a digital camera
# Specify the parent directory

$parentFolder = "main"

# Get all files from all subdirectories and move them to the parent directory
Get-ChildItem -Path $parentFolder -Recurse -File | Move-Item -Destination $parentFolder -Force

Write-Host "Finished moving files."
