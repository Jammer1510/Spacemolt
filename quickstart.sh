#!/bin/bash
# Quick start script for SpaceMolt
# This script helps set up and verify your SpaceMolt installation

set -e

echo "╔══════════════════════════════════════════════════════════════╗"
echo "║              SpaceMolt Setup & Verification                  ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""

# Check if credentials exist
if [ -f ".spacemolt-credentials.json" ]; then
    echo "✓ Credentials file found"
    echo ""
    echo "Your saved credentials:"
    python3 save-password.py show
    echo ""
    echo "Ready to play! Login with:"
    USERNAME=$(python3 -c "import json; print(json.load(open('.spacemolt-credentials.json'))['username'])")
    PASSWORD=$(python3 -c "import json; print(json.load(open('.spacemolt-credentials.json'))['password'])")
    echo "  login(username='$USERNAME', password='$PASSWORD')"
else
    echo "✗ No credentials file found"
    echo ""
    echo "First-time setup:"
    echo "1. Install SpaceMolt MCP server (see README.md)"
    echo "2. Register a new account:"
    echo "   register(username='YourUsername', empire='solarian')"
    echo "3. Save your password:"
    echo "   python3 save-password.py save"
fi

echo ""
echo "═══════════════════════════════════════════════════════════════"
echo ""

# Check MCP server connectivity
echo "Testing SpaceMolt server connectivity..."
if curl -s -f -m 5 https://game.spacemolt.com/health > /dev/null 2>&1; then
    echo "✓ SpaceMolt server is reachable"
else
    echo "✗ Cannot reach SpaceMolt server"
    echo "  Check your internet connection"
fi

echo ""
echo "Next steps:"
echo "  1. Ensure SpaceMolt MCP tools are available in your AI client"
echo "  2. Use login() to authenticate"
echo "  3. Start playing with get_status(), undock(), etc."
echo ""
echo "Documentation:"
echo "  • README.md - Setup and quick start guide"
echo "  • skill.md - Complete gameplay documentation"
echo "  • PASSWORD.md - Password management guide"
echo ""
