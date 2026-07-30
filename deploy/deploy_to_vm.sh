#!/bin/bash
set -e

VM_HOST="80.225.193.247"
VM_USER="ubuntu"
KEY_PATH="/Users/rama.m/workspace/personal/vm/mumbai_vm.key"
REMOTE_DIR="/home/ubuntu/astroavatar-reels"

echo "=========================================================="
echo "🚀 Updating AstroAvatar Reels Production on VM via Git"
echo "=========================================================="

echo "1. Triggering Git Pull on Remote VM ($VM_HOST)..."
ssh -i "$KEY_PATH" -o StrictHostKeyChecking=no $VM_USER@$VM_HOST "cd $REMOTE_DIR && git fetch origin && git reset --hard origin/main"

echo "2. Executing VM setup script on remote server..."
ssh -i "$KEY_PATH" -o StrictHostKeyChecking=no $VM_USER@$VM_HOST "bash $REMOTE_DIR/deploy/setup_vm.sh"

echo "=========================================================="
echo "🎉 Remote VM Updated via Git Successfully!"
echo "=========================================================="
