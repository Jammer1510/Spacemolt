#!/usr/bin/env python3
"""
SpaceMolt Player Agent
A simple agent that can play SpaceMolt autonomously with password persistence.
"""

import json
import os
import sys
from pathlib import Path


class SpaceMoltPlayer:
    """
    SpaceMolt player agent that handles authentication and gameplay.
    """
    
    CREDENTIALS_FILE = ".spacemolt-credentials.json"
    
    def __init__(self):
        self.credentials = None
        self.credentials_path = Path(__file__).parent / self.CREDENTIALS_FILE
    
    def load_credentials(self):
        """Load saved credentials from file."""
        if self.credentials_path.exists():
            try:
                with open(self.credentials_path, 'r') as f:
                    self.credentials = json.load(f)
                print(f"✓ Loaded credentials for user: {self.credentials.get('username')}")
                return True
            except Exception as e:
                print(f"✗ Error loading credentials: {e}")
                return False
        else:
            print(f"✗ No saved credentials found at {self.credentials_path}")
            return False
    
    def save_credentials(self, username, password, empire=None, playstyle=None):
        """Save credentials to file securely."""
        self.credentials = {
            "username": username,
            "password": password,
            "empire": empire or "solarian",
            "playstyle": playstyle or "miner"
        }
        
        try:
            # Write with restricted permissions
            with open(self.credentials_path, 'w') as f:
                json.dump(self.credentials, f, indent=2)
            
            # Set file permissions to user-only on Unix-like systems
            if os.name != 'nt':  # Not Windows
                os.chmod(self.credentials_path, 0o600)
            
            print(f"✓ Saved credentials for user: {username}")
            print(f"  Location: {self.credentials_path}")
            print(f"  ⚠️  IMPORTANT: Keep this password safe! There is NO password recovery.")
            return True
        except Exception as e:
            print(f"✗ Error saving credentials: {e}")
            return False
    
    def get_auth_info(self):
        """Get authentication info for login."""
        if not self.credentials:
            return None
        return {
            "username": self.credentials.get("username"),
            "password": self.credentials.get("password")
        }
    
    def display_welcome(self):
        """Display welcome message with instructions."""
        print("""
╔══════════════════════════════════════════════════════════════╗
║                    🚀 SPACEMOLT AGENT 🚀                      ║
╚══════════════════════════════════════════════════════════════╝

Welcome to SpaceMolt! This agent will help you play SpaceMolt
through the MCP (Model Context Protocol).

GETTING STARTED:
1. Make sure you have SpaceMolt MCP tools available
2. If not, install the MCP server (see README.md)
3. Run this agent to manage your credentials

IMPORTANT NOTES:
- Your password is a 256-bit token - there is NO recovery if lost!
- Credentials are saved locally in .spacemolt-credentials.json
- This file is in .gitignore - NEVER commit it to version control
- The agent uses standard MCP tools for all game interactions
""")
    
    def interactive_setup(self):
        """Interactive setup for new players."""
        print("\n=== SpaceMolt Account Setup ===\n")
        
        print("Choose your playstyle:")
        print("1. Miner/Trader - Extract resources, find profitable trade routes")
        print("2. Explorer - Chart distant systems, discover secrets")
        print("3. Pirate/Combat - Hunt players, loot wrecks, live dangerously")
        print("4. Stealth/Infiltrator - Operate in shadows, spy, ambush")
        print("5. Builder/Crafter - Construct stations, manufacture goods")
        
        playstyle_map = {
            "1": "miner",
            "2": "explorer",
            "3": "pirate",
            "4": "stealth",
            "5": "builder"
        }
        
        empire_map = {
            "miner": "solarian",
            "explorer": "nebula",
            "pirate": "crimson",
            "stealth": "voidborn",
            "builder": "outerrim"
        }
        
        choice = input("\nEnter choice (1-5): ").strip()
        playstyle = playstyle_map.get(choice, "miner")
        empire = empire_map[playstyle]
        
        print(f"\nSelected playstyle: {playstyle.upper()}")
        print(f"Recommended empire: {empire.upper()}")
        
        username = input("\nEnter your desired username: ").strip()
        
        print("\n⚠️  After registration, you will receive a 256-bit password.")
        print("   Save it immediately - there is NO password recovery!")
        print("\n   The agent will save it automatically to .spacemolt-credentials.json")
        
        return {
            "username": username,
            "empire": empire,
            "playstyle": playstyle
        }


def main():
    """Main entry point for the SpaceMolt agent."""
    player = SpaceMoltPlayer()
    player.display_welcome()
    
    # Check if credentials exist
    if player.load_credentials():
        auth = player.get_auth_info()
        print(f"\n✓ Ready to play as: {auth['username']}")
        print("\nNext steps:")
        print("1. Use SpaceMolt MCP tools in your AI client")
        print("2. Call login(username='{}', password='{}')".format(
            auth['username'], auth['password']))
        print("3. Start playing! Use get_status() to check your ship and location")
    else:
        print("\n✗ No credentials found. You need to:")
        print("1. Register a new account using SpaceMolt MCP tools")
        print("2. Save your password using this script")
        print("\nWould you like to set up credentials interactively? (y/n)")
        
        response = input().strip().lower()
        if response == 'y':
            setup_info = player.interactive_setup()
            print("\n" + "="*60)
            print("NEXT STEPS:")
            print("="*60)
            print(f"1. Use your AI client with SpaceMolt MCP tools")
            print(f"2. Register: register(username='{setup_info['username']}', empire='{setup_info['empire']}')")
            print(f"3. SAVE THE PASSWORD you receive!")
            print(f"4. Run this script again to save credentials")
            print("="*60)


if __name__ == "__main__":
    main()
