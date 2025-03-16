# RenameFiles
A python script to rename files in the working directory.

## Customization
The following variables can be updated to alter the functionality of this script.
| Variable | Description | Default Value |
| ----------- | ----------- | ----------- |
| length | The number of digits to include in the random prefix. The prefix will not be unique | 5 |
| nameBlacklist | The file names to ignore. Does not include extension. | [] |
| nameWhitelist | The file names to include. If not provided, all files will be included. Does not include extension. | [] |
| extensionBlacklist | The extensions to ignore. Includes leading period. | [".py"] |
| extensionWhitelist | The extensions to include. If not provided, all extensions will be included. Includes leading period. | [] |

## Usage
1. Drop 0-RenameFies.py into the target directory.
2. Shift + Right-click in the directory window.
3. Select `Open powershell window here`.
4. Enter the following: `python .\0-RenameFiles.py`.
5. Choose the appropriate action.