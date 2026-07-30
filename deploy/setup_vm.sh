#!/bin/bash
set -e

echo "=========================================================="
echo "🚀 Setting up AstroAvatar Automated Reels Production on VM"
echo "=========================================================="

APP_DIR="/home/ubuntu/astroavatar-reels"
mkdir -p "$APP_DIR"

cd "$APP_DIR"

echo "1. Installing Python dependencies..."
sudo apt-get update -y
sudo apt-get install -y python3-pip python3-venv ffmpeg
python3 -m pip install --upgrade pip
python3 -m pip install requests numpy

echo "2. Installing Node.js & Remotion dependencies..."
if [ -d "reels-factory" ]; then
    cd reels-factory
    npm install
    # Pre-download Chromium for Remotion
    npx remotion browser ensure
    cd ..
fi

echo "3. Creating log directory..."
mkdir -p logs

echo "4. Setting up Crontab Schedule (Runs 2x Daily at 08:00 AM & 18:00 PM)..."
CRON_JOB_1="0 8 * * * cd $APP_DIR && /usr/bin/python3 scripts/pipeline_runner.py >> $APP_DIR/logs/cron.log 2>&1"
CRON_JOB_2="0 18 * * * cd $APP_DIR && /usr/bin/python3 scripts/pipeline_runner.py >> $APP_DIR/logs/cron.log 2>&1"

(crontab -l 2>/dev/null | grep -v "pipeline_runner.py" ; echo "$CRON_JOB_1" ; echo "$CRON_JOB_2") | crontab -

echo "=========================================================="
echo "✅ VM Setup Complete! Crontab active."
echo "Current Crontab Schedule:"
crontab -l
echo "=========================================================="
