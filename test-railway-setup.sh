#!/bin/bash
# Railway Deployment Test Script
# This script simulates Railway's deployment process to test locally

echo "🚀 Testing Railway deployment setup..."
echo ""

# Check required files
echo "📁 Checking deployment files..."
if [ ! -f "Procfile" ]; then
    echo "❌ Procfile not found!"
    exit 1
fi
echo "✅ Procfile found"

if [ ! -f "railway.json" ]; then
    echo "❌ railway.json not found!"
    exit 1
fi
echo "✅ railway.json found"

if [ ! -f "requirements.txt" ]; then
    echo "❌ requirements.txt not found!"
    exit 1
fi
echo "✅ requirements.txt found"

if [ ! -f "main.py" ]; then
    echo "❌ main.py not found!"
    exit 1
fi
echo "✅ main.py found"

echo ""

# Test PORT variable handling
echo "🔧 Testing PORT environment variable handling..."
export PORT=3001
echo "Setting PORT to $PORT"

# Start the application in background
python main.py &
APP_PID=$!

# Wait for startup
sleep 3

# Test the endpoint
echo "📡 Testing application on port $PORT..."
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:$PORT 2>/dev/null)

if [ "$HTTP_CODE" = "200" ]; then
    echo "✅ Application responds with HTTP $HTTP_CODE"
else
    echo "❌ Application failed to respond (HTTP $HTTP_CODE)"
    kill $APP_PID 2>/dev/null
    exit 1
fi

# Clean up
kill $APP_PID 2>/dev/null
wait $APP_PID 2>/dev/null

echo ""
echo "🎉 All tests passed! Your app is ready for Railway deployment."
echo ""
echo "Next steps:"
echo "1. Push your code to GitHub"
echo "2. Connect your repository to Railway"
echo "3. Deploy!"