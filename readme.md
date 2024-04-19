### This script cycles the power profiles of a Linux system running PoP-OS. It will not work for other distros.

It works by fetching the current power profile, and based on the output it switches the profile to the next in line, e.g. `battery -> balanced -> performance`. For each profile a screen brightness is set, using brightnessctl, which you can get with the command:

```bash
sudo apt-get update -y

sudo apt-get install -y brightnessctl
```


### How to use this script
1. Make sure you have the `brightnessctl` package.
2. Clone this repository.
3. Run the following command:
    ```bash
    echo -e '#!/bin/bash\npython3 /path_to_repo/main.py' > /path_to_repo/run.sh
    ```
    This will create a bash script in the repo that executes the python script.
4. Run the following commands:
    ```bash
    sudo chown root:root /path_to_repo/run.sh
    sudo chmod 700 /path_to_repo/run.sh
    ```
    The above command will make the script executable and change its ownership to root.

5. Set up sudo to allow run.sh to execute without requiring password:
    ```bash
    sudo visudo
    ```

    locate `%sudo ALL=(ALL:ALL) ALL`
    
    below that, insert the following:

    `username  ALL=(ALL) NOPASSWD: /path_to_repo/run.sh`

    replace 'username' with your username.

6. OPTIONAL: Open 'Keyboard' settings in the Gnome settings panel, and create a custom shortcut the calls the script. The script can be called with the following command:
    `sudo path_to_repo/run.sh`


Rejoice, you should now be able to swap the power profile and brightness of your screen with a keyboard shortcut. To set a different brightness for each power profile you will need to edit the lines in the code that looks like this:

```python
subprocess.run(["sudo", "brightnessctl", "-d", "amdgpu_bl1", "set", "50%"], check=True)

# change 50% to whatever value you would like to be set for screen brightness.
```