
# -- Init -- #
# To ensure if using same metadata
if [ -f "poetry.lock" ]; then
    CONTENT_HASH=$(grep 'content-hash' poetry.lock | awk '{print $3}' | tr -d '"')
    sudo rm poetry.lock

poetry lock
echo "\n[Done] poetry.lock initialized"
fi

# Reset Project
sudo rm -r dist
sudo rm -r optimizean/__pycache__ 

# Initialize Project
poetry build; pip install ./dist/optimizean-1.1.1-py3-none-any.whl
echo "\n[Done] Initialize Project"
sleep 3

MAX_LEVEL=2
current_level=0

while [ $current_level -lt $MAX_LEVEL ]; do

    # -- Run -- #
    clear
    echo "Current Path is $(pwd)"
    sleep 1
    
    yes | optimizean
    
    cd ..
    current_level=$((current_level + 1))
    
    sleep 3
    clear

done