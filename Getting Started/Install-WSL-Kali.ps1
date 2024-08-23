Clear-Host
if ((Get-ExecutionPolicy -Scope CurrentUser) -eq "Undefined"){
    Write-Host -Object "If you are seeing this message please open a PowerShell terminal as Administartor and run the following command before continuing.`n`nSet-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted"
}
Import-Module -Name WindowsUpdate

$Arguments = '-Command "$NumberOfUpdates=(Get-WindowsUpdate -WithHidden -Verbose|Measure-Object -Line).Lines
    if ($NumberOfUpdates -ne 0) {
        $Mesg = (echo "You have $($NumberOfUpdates) update that need to be installed.")
        Write-Host -Object $Mesg
        Install-WindowsUpdate -MicrosoftUpdate -AcceptAll -Verbose
    }
    dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
    dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all
    wsl --set-default-version 2
    wsl --update
    $Mesg = (echo "`nKali-Linux will install next, after you enter a user name and password, please type exit to continue the installation.`n")
    Write-Host -Object $Mesg
    pause
    wsl --install kali-linux
    wsl --set-default kali-linux
    wsl --distribution kali-linux -- touch ~/.hushlogin
    wsl --distribution kali-linux -- sudo touch ~/.hushlogin
    wsl --distribution kali-linux -- sudo apt update
    wsl --distribution kali-linux -- sudo apt upgrade -y
    wsl --distribution kali-linux -- sudo apt install -y tmux neofetch nano nmap
    "'

Start-Process -FilePath powershell.exe -ArgumentList $Arguments -Verb RunAs -Wait

Write-Host -Object "A restart is required to finish the insallation."
$Restart = Read-Host -Prompt "Would you like to restart now? [Y|n]"
if ($Restart -notlike "n" -or $Restart -like "y"){
    while ($Restart -notlike "n" -and $Restart -notlike "y"){
        $Restart = Read-Host -Prompt "Would you like to restart now? [Y|n]"
    }
    if ($Restart -like "y") {
        Restart-Computer -Force
    }
}
