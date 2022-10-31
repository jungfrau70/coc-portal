#################################################################################################
# 1. Install WSL2 on Window10
#################################################################################################

https://pureinfotech.com/install-windows-subsystem-linux-2-windows-10/#:~:text=To%20install%20WSL2%20on%20Windows,%E2%80%9Cwsl%20%E2%80%93update%E2%80%9D%20command.

#################################################################################################
# 2. Install Unbuntu
#################################################################################################

https://learn.microsoft.com/ko-kr/windows/wsl/tutorials/gui-apps

#################################################################################################
# 3. Updating Ubuntu
#################################################################################################

# https://medium.com/@japheth.yates/the-complete-wsl2-gui-setup-2582828f4577

sudo apt update && sudo apt -y upgrade
sudo apt install build-essential
sudo apt install net-tools
sudo apt install xrdp -y && sudo systemctl enable xrdp


#################################################################################################
# 4. Setting up the GUI
#################################################################################################

sudo apt install -y tasksel
sudo tasksel install xubuntu-desktop
sudo apt install gtk2-engines

export DISPLAY=$(cat /etc/resolv.conf | grep nameserver | awk '{print $2; exit;}'):0.0
export LIBGL_ALWAYS_INDIRECT=1
sudo /etc/init.d/dbus start &> /dev/null

cat <<EOF >>/etc/sudoers.d/dbus
ubuntu ALL = (root) NOPASSWD: /etc/init.d/dbus
EOF


#################################################################################################
# 5. Setting up X-server on Windows 10
#################################################################################################

# https://medium.com/@japheth.yates/the-complete-wsl2-gui-setup-2582828f4577

#################################################################################################
# 6. Start App
#################################################################################################

gedit &
firefox &


#################################################################################################
# 7. Setup vscode with remote-wsl
#################################################################################################

https://code.visualstudio.com/docs/setup/windows

# Additionally install remote-wsl
