#################################################################################################
# Check python version && create symbolic link
#################################################################################################

python3 --version
cd /usr/bin
ls -al python*
sudo ln -s python3 python

#################################################################################################
# Create virtual environemnt
#################################################################################################

mkdir -p ~/lenz/backend && cd ~/lenz/backend
python -m venv venv [--copies]
source venv/bin/activate
(venv) pip install -r requirements.txt

# Optionally, tar venv-backend.tar
tar xpf venv-backend.tar
source venv/bin/activate
