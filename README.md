# BootShield 🔒  
_A Windows security script that requires a password during startup to prevent unauthorized access._
---
## 📖 Description  
BootShield is a Python script designed to add a layer of security to your Windows system. When placed in the Startup folder, it gives users **100 seconds** to enter a predefined password after login. If the password is not entered, the system shuts down automatically.

### Steps 
1. **Configure the password**:
Open BootShield.py and change the PASSWORD variable (default: 1234).
2. **Place the script in the Startup folder**:
Press Win + R, paste this path:
%appdata%\Microsoft\Windows\Start Menu\Programs\Startup
Copy BootShield.py into this folder.