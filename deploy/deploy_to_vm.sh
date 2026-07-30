#!/bin/bash
set -e

VM_HOST="80.225.193.247"
VM_USER="ubuntu"
KEY_PATH="/Users/rama.m/workspace/personal/vm/mumbai_vm.key"
REMOTE_DIR="/home/ubuntu/astroavatar-reels"

echo "=========================================================="
echo "🚀 Deploying AstroAvatar Reels Production System to VM"
echo "=========================================================="

echo "1. Syncing project files to VM ($VM_HOST)..."
rsync -avz -e "ssh -i $KEY_PATH -o StrictHostKeyChecking=no" \
  --exclude 'node_modules' \
  --exclude '.git' \
  --exclude 'out' \
  --exclude '.DS_Store' \
  ./ $VM_USER@$VM_HOST:$REMOTE_DIR/

echo "2. Executing VM setup script on remote server..."
ssh -i "$KEY_PATH" -o StrictHostKeyChecking=no $VM_USER@$VM_HOST "bash $REMOTE_DIR/deploy/setup_vm.sh"

echo "=========================================================="
echo "🎉 Deployment to VM Successful!"
echo "=========================================================="
