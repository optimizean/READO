
# -- Init -- #
# To ensure if using same metadata
if [ -f "poetry.lock" ]; then
    CONTENT_HASH=$(grep 'content-hash' poetry.lock | awk '{print $3}' | tr -d '"')
else
    poetry add requests
    poetry add rich
    poetry lock
fi

# Reset Project
sudo rm -r dist
cd optimizean
sudo rm -r __pycache__ 
cd ..

# Initialize Project
poetry build
pip install .
echo "[Done] Initialized Project"
sleep 3


MAX_LEVEL=3
current_level=0

while [ $current_level -lt $MAX_LEVEL ]; do

    # -- Run -- #
    echo "Current Path is $(pwd)"
    yes | optimizean
    cd ..
    current_level=$((current_level + 1))
    
    sleep 3
    clear

done