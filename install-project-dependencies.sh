#!/usr/bin/env sh

# Detect OS and store in variable
if [ "$(uname)" = "Darwin" ]; then
    OS="mac"
elif [ "$(expr substr $(uname -s) 1 5)" = "Linux" ]; then
    OS="linux"
elif [ "$(expr substr $(uname -s) 1 10)" = "MINGW32_NT" ] || [ "$(expr substr $(uname -s) 1 10)" = "MINGW64_NT" ]; then
    OS="windows"
else
    echo "Unsupported operating system"
    exit 1
fi

pip install -r requirements/${OS}/requirements.txt