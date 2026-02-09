#!/usr/bin/env python3
"""
Quick utility to save SpaceMolt credentials after registration.
"""

import json
import os
import sys
from pathlib import Path


def save_password():
    """Save SpaceMolt password after registration."""
    print("╔══════════════════════════════════════════════════════════╗")
    print("║          SpaceMolt Password Manager                      ║")
    print("╚══════════════════════════════════════════════════════════╝\n")
    
    credentials_file = Path(".spacemolt-credentials.json")
    
    # Check if credentials already exist
    if credentials_file.exists():
        print(f"⚠️  Credentials file already exists: {credentials_file}")
        response = input("Do you want to update it? (y/n): ").strip().lower()
        if response != 'y':
            print("Cancelled.")
            return
    
    print("\nAfter registering with SpaceMolt, enter your details:\n")
    
    username = input("Username: ").strip()
    if not username:
        print("✗ Username cannot be empty!")
        return
    
    password = input("Password (256-bit token): ").strip()
    if not password:
        print("✗ Password cannot be empty!")
        return
    
    empire = input("Empire (solarian/nebula/crimson/voidborn/outerrim) [solarian]: ").strip() or "solarian"
    playstyle = input("Playstyle (miner/explorer/pirate/stealth/builder) [miner]: ").strip() or "miner"
    
    # Save credentials
    credentials = {
        "username": username,
        "password": password,
        "empire": empire,
        "playstyle": playstyle
    }
    
    try:
        with open(credentials_file, 'w') as f:
            json.dump(credentials, f, indent=2)
        
        # Set restrictive permissions on Unix-like systems
        if os.name != 'nt':
            os.chmod(credentials_file, 0o600)
        
        print(f"\n✓ Credentials saved to {credentials_file}")
        print(f"✓ Username: {username}")
        print(f"✓ Empire: {empire}")
        print(f"✓ Playstyle: {playstyle}")
        print("\n⚠️  IMPORTANT: Keep this file safe! Password recovery is NOT possible!")
        print("\nYou can now login by loading credentials from file:")
        print("  import json")
        print("  with open('.spacemolt-credentials.json') as f:")
        print("      creds = json.load(f)")
        print(f"  login(username=creds['username'], password=creds['password'])")
        
    except Exception as e:
        print(f"\n✗ Error saving credentials: {e}")
        return


def show_credentials():
    """Display saved credentials (password masked)."""
    credentials_file = Path(".spacemolt-credentials.json")
    
    if not credentials_file.exists():
        print("✗ No credentials file found!")
        print(f"  Expected location: {credentials_file}")
        return
    
    try:
        with open(credentials_file, 'r') as f:
            creds = json.load(f)
        
        print("\n═══ Saved Credentials ═══")
        print(f"Username:  {creds.get('username', 'N/A')}")
        print(f"Empire:    {creds.get('empire', 'N/A')}")
        print(f"Playstyle: {creds.get('playstyle', 'N/A')}")
        print(f"Password:  {'*' * 20}... (masked)")
        print("\nTo see full password, view the file directly:")
        print(f"  cat {credentials_file}")
        
    except Exception as e:
        print(f"✗ Error reading credentials: {e}")


def main():
    """Main menu."""
    if len(sys.argv) > 1:
        if sys.argv[1] == "show":
            show_credentials()
            return
        elif sys.argv[1] == "save":
            save_password()
            return
        else:
            print(f"Unknown command: {sys.argv[1]}")
            print("Usage: python3 save-password.py [save|show]")
            return
    
    # Interactive menu
    print("\nSpaceMolt Password Manager")
    print("-" * 40)
    print("1. Save new credentials")
    print("2. Show saved credentials")
    print("3. Exit")
    
    choice = input("\nChoice: ").strip()
    
    if choice == "1":
        save_password()
    elif choice == "2":
        show_credentials()
    elif choice == "3":
        print("Goodbye!")
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
