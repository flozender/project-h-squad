tmux kill-server
source python3-virtualenv/bin/activate
cd project-h-squad
git fetch && git reset origin/main --hard
pip install -r requirements.txt
tmux new -d flask run --host=0.0.0.0
