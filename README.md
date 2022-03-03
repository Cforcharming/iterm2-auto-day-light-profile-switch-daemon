# iterm2-auto-day-light-profile-switch-daemon
This script detects the dark/light theme mode of macOS >= 10.14 Mojave continuously, then switch iTerm2 profile correspondingly.

This script runs forever as daemon when iTerm2, if it is put into ~/Library/Applicatoin Support/iTerm2/Scripts/AutoLaunch
Or this script runs forever as daemon when clicked, if it is put into ~/Library/Applicatoin Support/iTerm2/Scripts

Customization: 

Change the value of variable <code>light_profile_name = "YOUR_LIGHT_PROFILE_NAME_HERE"</code> on line 30 to your own light theme profile name.
Change the value of variable <code>dark_profile_name = "YOUR_DARK_PROFILE_NAME_HERE"</code> on line 31 to your own dark theme profile name.
Change the variable <code>refresh_sec</code> on line 34 to  customize the refresh inverval, which is 0.1 second by default.
