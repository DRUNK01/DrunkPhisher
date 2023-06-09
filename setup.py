# A OmniTotal Code

import subprocess as sb
import os, time

uname = sb.getoutput("uname -m")
chroot = sb.getoutput("command -v termux-chroot")
binPath = "/data/data/com.termux/files/usr/bin/"

# Download the File
def download(url):
    os.system("wget \"" + url + "\" --no-check-certificate --show-progress")
    return url.split("/")[-1]

# Install Package
def install(pkg):
    print("\n[\033[92m!\033[37m] Installing " + pkg + "...\n")
    os.system("pkg install " + pkg + " -y")

# Install Ngrok
def install_Ngrok():
    print("\n[\033[92m!\033[37m] Installing Ngrok")
    if os.path.exists(binPath+"ngrok"):
        time.sleep(1)
        print("\n[\033[92m!\033[37m] Ngrok is already Installed")
        return
    
    if (uname == "arm") or (uname == "Android"):
        file = download("https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip")
    elif (uname == "aarch64"):
        file = download("https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm64.zip")
    elif (uname == "x86_64"):
        file = download("https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip")
    else:
        file = download("https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-386.zip")
    
    if not os.path.exists(file):
       print("\n[\033[91m!\033[37m] Ngrok install Error")
       print("[*] Install Manually")
       return
    
    os.system("unzip " + file + " > /dev/null 2>&1")
    os.system("mv -f ngrok " + binPath + "ngrok")
    os.system("chmod +x " + binPath+ "ngrok")
    os.system("rm -rf " + file)
    
    print("\n[\033[92m!\033[37m] Ngrok install Complete")


# Install Cloudflared
def install_Cloudflared():
    print("\n[\033[92m!\033[37m] Installing Cloudflared")
    if os.path.exists(binPath+"cloudflared"):
        time.sleep(1)
        print("\n[\033[92m!\033[37m] Cloudflared is Installed")
        return
    
    if (uname == "arm") or (uname == "Android"):
        file = download("https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm")
    elif (uname == "aarch64"):
        file = download("https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm64")
    elif (uname == "x86_64"):
        file = download("https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64")
    else:
        file = download("https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-386")
    
    if not os.path.exists(file):
       print("\n[\033[91m!\033[37m] Claudflared install Error")
       print("[*] Install Manually")
       return
    
    os.system("mv -f " + file + " " + binPath + "cloudflared > /dev/null 2>&1")
    os.system("chmod +x " + binPath + "cloudflared")
    print("\n\033[92m!\033[37m] Cloudflared Install Complete")

# Generate ssh key for localhost.run
def install_LocalhostRun():
    print("\n[\033[92m!\033[37m] Installing Localhost.run")
    
    if not (os.path.exists("/data/data/com.termux/files/home/.ssh")):
        os.system("mkdir /data/data/com.termux/files/home/.ssh")
    
    if not (os.path.exists("/data/data/com.termux/files/home/.ssh/known_hosts")):
        os.system("touch /data/data/com.termux/files/home/.ssh/known_hosts")
    
    if not (sb.getoutput("ssh-keygen -F localhost.run") == ""):
        time.sleep(1)
        print("\n[\033[92m!\033[37m] Localhost.run is Installed")
        return
    
    os.system("ssh-keyscan -H localhost.run >> /data/data/com.termux/files/home/.ssh/known_hosts")
    print("\n\033[92m!\033[37m] Localhost.run Install Complete")


# Install Required Packages
def install_Setup():
    print("\n[\033[92m!\033[37m] Update and Upgrading...\n")
    os.system("apt update -y && apt upgrade -y")
    install("python")
    install("wget")
    install("curl")
    install("unzip")
    install("proot resolv-conf")

print("\n[\033[92m*\033[37m] Please Stand By")
print("\n[*] Installing Packages")
time.sleep(1)

install_Setup()
install_Ngrok()
time.sleep(0.5)
install_Cloudflared()
install_LocalhostRun()

print("\n[\033[93m!\033[37m] Installation Complete!\n")