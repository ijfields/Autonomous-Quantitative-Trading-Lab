#!/bin/bash

# Ensure PM2 is installed
if ! command -v pm2 &> /dev/null
then
    echo "PM2 is not installed. Installing globally..."
    npm install -g pm2
fi

# Navigate to dashboard directory
cd research_backtesting_dashboard

# Start the dashboard using PM2
echo "Starting dashboard with PM2..."
pm2 start npm --name "dashboard" -- run dev

# Save PM2 process list
pm2 save

echo "Dashboard started! Access it at http://localhost:3000 (or your server IP:3000)"
