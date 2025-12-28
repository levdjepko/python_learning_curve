# TODO: Define your source and destination paths here
$sourcePath = "C:\PHOTOS\All Pictures From Canon IXUS"
$destPath = "C:\PHOTOS\All Pictures From Canon IXUS\Combined"

# Create the destination folder if it doesn't already exist
if (!(Test-Path -Path $destPath)) {
    New-Item -ItemType Directory -Path $destPath
}

# Define the image/video extensions you want to move
$extensions = @("*.jpg", "*.jpeg", "*.png", "*.gif", "*.tiff", "*.heic", "*.mov")

# Find and move the files
Get-ChildItem -Path $sourcePath -Include $extensions -Recurse | ForEach-Object {
    $destFile = Join-Path -ChildPath $_.Name -Path $destPath
    
    # Check for duplicate filenames to avoid overwriting
    if (Test-Path -Path $destFile) {
        $newName = "{0}_{1}{2}" -f $_.BaseName, (Get-Random), $_.Extension
        Move-Item -Path $_.FullName -Destination (Join-Path -Path $destPath -ChildPath $newName)
    } else {
        Move-Item -Path $_.FullName -Destination $destPath
    }
}

Write-Host "Mission accomplished! All photos moved to $destPath" -ForegroundColor Green
