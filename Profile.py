#!/usr/bin/env python3.10

# Copyright (C) 2022 https://github.com/cforcharming
# 
# This software is under MIT License.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in the
# Software without restriction, including without limitation the rights to use, copy,
# modify, merge, publish, distribute, sublicense, and/or sell copies of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
# CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
# OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import subprocess
import time
import iterm2

# This script runs forever as daemon when started.
# If it is put into ~/Library/Applicatoin Support/iTerm2/Scripts/AutoLaunch
# then it will start automatically.
# This script detects the dark/light theme mode of macOS >= 10.14 Mojave continuously,
# then switch the profile correspondingly.

# custom your theme name here.
light_profile_name = 'Light'
dark_profile_name = 'Dark'

# custom the refresh time in seconds here.
refresh_sec = 0.1

def get_current_theme():
    cur_std=subprocess.run(['/usr/bin/defaults', 'read', '-g', 'AppleInterfaceStyle'], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    current=cur_std.stdout.decode('utf-8').strip()
    if current == '':
        current=light_profile_name
    else:
        current=dark_profile_name
    return current

def get_current_session(app):
    
    current_session = None
    window = app.current_terminal_window   
    if window is not None:
        tab = window.current_tab
        if tab is not None:
            current_session = tab.current_session

    return current_session

def get_partial(partial_profiles, current):
    
    # Iterate over each partial profile
    for partial in partial_profiles:   
        
        if partial.name == current:
        # This is the one we're looking for. Change the current session's
        # profile.  
            return partial
        
    return None

async def main(connection):
    
    # Query for the list of profiles so we can search by name. This returns a
    # subset of the full profiles so it's fast.
    partial_profiles = await iterm2.PartialProfile.async_query(connection)
    
    current = get_current_theme()
    partial = get_partial(partial_profiles, current)  
    if partial is not None:
        await partial.async_make_default()

    app = await iterm2.async_get_app(connection) 
    
    while True:
        
        try:
            current_session = get_current_session(app)
            if current_session is None:
                time.sleep(refresh_sec)
                app = await iterm2.async_get_app(connection) 
                continue

            current = get_current_theme()
            current_profile = await current_session.async_get_profile()
            current_profile_name = current_profile.all_properties['Name']

            if current != current_profile_name:
                
                partial = get_partial(partial_profiles, current)  
                if partial is not None:
                    await partial.async_make_default()
                    full = await partial.async_get_full_profile()
                    current_session = get_current_session(app)
                    await current_session.async_set_profile(full)
        
        except iterm2.rpc.RPCException:
            pass

        time.sleep(refresh_sec)

# This instructs the script to run the "main" coroutine and to keep running even after it returns.
iterm2.run_forever(main)

