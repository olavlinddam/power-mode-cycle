import subprocess

# Execute the system76-power profile command and capture the output
try:
    process = subprocess.run(["system76-power", "profile"], capture_output=True, text=True)
    output = process.stdout
except subprocess.CalledProcessError as e:
    print(f"Error executing system76-power profile: {e}")
    exit(1)

if 'Performance' in output:
    try:
        subprocess.run(["system76-power", "profile", "battery"], check=True)
        subprocess.run(["sudo", "brightnessctl", "-d", "amdgpu_bl1", "set", "50%"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error setting power profile or brightness: {e}")
elif 'Battery' in output:
    try:
        subprocess.run(["system76-power", "profile", "balanced"], check=True)
        subprocess.run(["sudo", "brightnessctl", "-d", "amdgpu_bl1", "set", "75%"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error setting power profile or brightness: {e}")
else:
    try:
        subprocess.run(["system76-power", "profile", "performance"], check=True)
        subprocess.run(["sudo", "brightnessctl", "-d", "amdgpu_bl1", "set", "100%"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error setting power profile or brightness: {e}")