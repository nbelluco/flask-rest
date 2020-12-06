echo "Installing virtualenv in .venv folder"

python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
deactivate

echo "SUCCESS: virtualenv installed."
echo "run 'source .venv/bin/activate' to enable it"
exit 0
