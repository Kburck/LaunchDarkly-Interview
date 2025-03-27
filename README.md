# LaunchDarkly-Interview
Interview Materials for Launch Darkly

# LaunchDarkly Interview Assignment

This project demonstrates the use of LaunchDarkly feature flags for **Release & Remediation** and **Targeting**.

## 🚀 Features
- **Release & Remediate:** enable/disable a feature using feature flags.
- **Targeting:** Control feature access based on user attributes (e.g., role, email, region, name).
  
## 🛠️ Setup Instructions
### 1️⃣ Prerequisites
- Python 3 installed
- LaunchDarkly account with an SDK key

### 2️⃣ Install Dependencies
Run:
```sh
pip install -r requirements.txt

```
Replace <my-sdk-key> in main2.py with your actual LaunchDarkly SDK key

Run the Script
Run:
```sh
python main.py
```
This will check the feature flag state and update in real time.

### Test Targeting
Modify main.py to change the user's role:

.set("role", "admin")  # Change to "member" or "guest" to test targeting

Then, update LaunchDarkly targeting rules accordingly.

## Ctrl+C to stop the script

Adjust the targeting rules in LD UI to adjust who you're targeting

This determines the feature flag behaviour

