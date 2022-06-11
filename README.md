# iterm2-auto-day-light-profile-switch-daemon
This script detects the dark/light theme mode of macOS >= 10.14 Mojave continuously, then switch iTerm2 profile correspondingly.

This script runs forever as daemon when iTerm2, if it is put into `~/Library/Application Support/iTerm2/Scripts/AutoLaunch`

Or this script runs forever as daemon when clicked, if it is put into `~/Library/Application Support/iTerm2/Scripts`

## Install:
1. Get the script
```sh
git clone https://github.com/Cforcharming/iterm2-auto-day-light-profile-switch-daemon.git ~/Library/Application\ Support/iTerm2/Scripts/AutoLaunch/auto-day-light-profile-switch
```

2. Run it by clicking: Scripts -> AutoLaunch -> auto-day-light-profile-switch -> Profile.py

## Customization:

Change the value of variable `light_profile_name = "YOUR_LIGHT_PROFILE_NAME_HERE"` on line 30 to your own light theme profile name.

Change the value of variable `dark_profile_name = "YOUR_DARK_PROFILE_NAME_HERE"` on line 31 to your own dark theme profile name.
Change the variable refresh_sec on line 34 to  customize the refresh interval, which is 0.1 second by default.
