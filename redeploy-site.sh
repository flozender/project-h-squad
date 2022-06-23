source ../python3-virtualenv/bin/activate
git fetch && git reset origin/main --hard
pip install -r requirements.txt
systemctl daemon-reload
systemctl restart myportfolio
