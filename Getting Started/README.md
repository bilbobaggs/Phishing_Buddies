This script requires administrative privileges. Additionally, if you want to sright run it, you must first run "Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted" in an administrator terminal window.

On my slow virtual machine that I used to test, it take a few hours for the install to complete. Also, be prepared for it to take about 4 reboots.

Once you have it downloaded, you can try using the right click "Run With PowerShell" context menu option. The way I ran was to download it and enter the path in terminal.

`PS C:\Users\USERNAME> Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted`
`PS C:\Users\USERNAME> .\Downloads\Install-WSL-Kali.ps1`
