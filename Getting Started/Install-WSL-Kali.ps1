param (
	[Init32]$Stage
)

Clear-Host

<#--------------------#
If you are having trouble running this script due to an execution policy error, please run the following:

Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted
#--------------------#>

function Get-ScriptDirectory
{
  $Invocation = (Get-Variable MyInvocation -Scope 1).Value
  $Invocation.MyCommand.Path
}

$RunOnceKeyLocation = 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce' 

if ($Stage -eq $null -or $Stage -eq 0){
	$Arguments = ' -Command " 
		Install-Module -Name PSWindowsUpdate -Force
		Import-Module -Name WindowsUpdate

		# Going to give it a moment to start up all required services.
		Start-Sleep -Seconds 120

		$NumberOfUpdates = (Get-Windowsupdate -MicrosoftUpdate -AcceptAll|Measure-Object -Line).Lines

    		if ($NumberOfUpdates -ne 0) {
    		    $Mesg = (echo "Installing your missing update(s).")
    		    Write-Host -Object $Mesg
    		    Install-WindowsUpdate -MicrosoftUpdate -AcceptAll -Verbose
    		}"
	'

	Start-Process -FilePath powershell.exe -ArgumentList $Arguments -Verb RunAs -Wait
	$KeyEntry = "C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe -ExecutionPolicy Bypass -NoExit -Command `" & $(Get-ScriptDirectory) -Stage 1`""
	Set-ItemProperty -Path $RunOnceKeyLocation -Name Install-WSL -Value $KeyEntry
	Restart-Computer -Force
}

#$Stage = 1

if ($Stage -eq 1){
	$Arguments = '-Command "dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
    		dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all"
	'

	$KeyEntry = "C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe -ExecutionPolicy Bypass -NoExit -Command `" & $(Get-ScriptDirectory) -Stage 2`""
	Set-ItemProperty -Path $RunOnceKeyLocation -Name Install-WSL -Value $KeyEntry
	Start-Process -FilePath powershell.exe -ArgumentList $Arguments -Verb RunAs -Wait
}

#$Stage = 2

if ($Stage -eq 2){
	$Arguments = '-Command "wsl --set-default-version 2
	    wsl --update
	    $Mesg = (echo "`nKali-Linux will install next, after you enter a user name and password, please type exit to continue the installation.`n")
	    Write-Host -Object $Mesg
	    pause
	    wsl --install -d kali-linux
	    wsl --set-default kali-linux
	    wsl --distribution kali-linux -- touch ~/.hushlogin
	    wsl --distribution kali-linux -- sudo touch ~/.hushlogin
	    wsl --distribution kali-linux -- sudo apt update
	    wsl --distribution kali-linux -- sudo apt upgrade -y
	    wsl --distribution kali-linux -- sudo apt install -y fastfetch nmap
	"'
	
	Start-Process -FilePath powershell.exe -ArgumentList $Arguments -Verb RunAs -Wait
}
	
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
