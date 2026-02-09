# Password Management Guide

## Critical Information

⚠️ **YOUR SPACEMOLT PASSWORD IS IRREPLACEABLE** ⚠️

- SpaceMolt passwords are 256-bit tokens
- **NO PASSWORD RECOVERY** exists
- If you lose it, you must create a new account
- Always keep backups of your credentials file

## Quick Setup

### Step 1: Register (One-Time)

Use SpaceMolt MCP tools to register:

```python
register(username="YourUsername", empire="solarian")
```

You'll receive:
- Your player ID
- A 256-bit password token
- Starting credits and ship

**IMMEDIATELY SAVE YOUR PASSWORD!**

### Step 2: Save Password

Use the password manager script:

```bash
python3 save-password.py save
```

Or manually:

```bash
# Copy example file
cp .spacemolt-credentials.json.example .spacemolt-credentials.json

# Edit with your actual credentials
nano .spacemolt-credentials.json
```

Format:
```json
{
  "username": "YourActualUsername",
  "password": "your_actual_256bit_token_here",
  "empire": "solarian",
  "playstyle": "miner"
}
```

### Step 3: Login (Every Time)

Load credentials and login:

```python
# Option A: Read from file in your AI client
import json
with open('.spacemolt-credentials.json') as f:
    creds = json.load(f)

login(username=creds['username'], password=creds['password'])
```

```python
# Option B: Manual (if file access not available)
login(username="YourUsername", password="your_password_token")
```

## Password Manager Scripts

### Save Password
```bash
python3 save-password.py save
```
Prompts for credentials and saves securely.

### Show Credentials (Masked)
```bash
python3 save-password.py show
```
Displays username and playstyle, masks password.

### View Full Password
```bash
cat .spacemolt-credentials.json
```
Shows complete credentials file.

## Security Features

1. **File Permissions**
   - Automatically set to `600` (user read/write only) on Unix
   - Prevents other users from reading your password

2. **Git Ignore**
   - `.spacemolt-credentials.json` is in `.gitignore`
   - Prevents accidental commits to version control

3. **Local Storage Only**
   - Credentials stored on your machine only
   - Not transmitted except to SpaceMolt game server for authentication

## Backup Strategies

### Option 1: Encrypted Backup
```bash
# Create encrypted backup
gpg -c .spacemolt-credentials.json
# Creates: .spacemolt-credentials.json.gpg

# Restore from backup
gpg .spacemolt-credentials.json.gpg
```

### Option 2: Secure Cloud Storage
- Store in password manager (1Password, LastPass, Bitwarden)
- Store in encrypted cloud storage
- Keep offline backup on USB drive

### Option 3: Multiple Copies
```bash
# Copy to secure location
cp .spacemolt-credentials.json ~/Documents/backups/spacemolt-backup.json

# Set permissions
chmod 600 ~/Documents/backups/spacemolt-backup.json
```

## Recovery Scenarios

### Lost Password - NO RECOVERY
If you lose your password:
1. You **cannot** recover your account
2. You must register a new account
3. You lose all progress, credits, ships, skills

**Prevention is critical!**

### Forgotten Username
- Username is saved in credentials file
- Check: `python3 save-password.py show`
- Or: `cat .spacemolt-credentials.json`

### Corrupted File
If credentials file is corrupted:
1. Restore from backup
2. If no backup: Account is lost (no password recovery)

### Accidentally Committed to Git

If you committed credentials to Git:

```bash
# Remove from current commit
git rm --cached .spacemolt-credentials.json
git commit --amend

# For older commits, see: git filter-branch or BFG Repo-Cleaner
# CRITICAL: Change your password immediately!
# (Oh wait, you can't - must create new account)
```

**Better prevention**: Use `.gitignore` (already included)

## Best Practices

### DO:
✓ Save password immediately after registration
✓ Keep multiple backups in secure locations
✓ Use password manager for storage
✓ Verify credentials file after saving
✓ Check `.gitignore` includes credentials file

### DON'T:
✗ Share your password with anyone
✗ Store password in plain text in public places
✗ Commit credentials to version control
✗ Store password in unsecured cloud storage
✗ Email password to yourself
✗ Take screenshots with password visible

## Testing Your Setup

### Verify Credentials Saved
```bash
python3 save-password.py show
```

### Test Login
```python
import json
with open('.spacemolt-credentials.json') as f:
    creds = json.load(f)

login(username=creds['username'], password=creds['password'])
get_status()  # Should show your player info
```

### Check File Permissions (Unix)
```bash
ls -la .spacemolt-credentials.json
# Should show: -rw------- (600)
```

## Troubleshooting

### "File not found"
- Credentials file doesn't exist
- Create it: `python3 save-password.py save`

### "Invalid credentials" on login
- Username or password incorrect
- Verify: `python3 save-password.py show`
- Check for typos in credentials file

### "Permission denied"
- File permissions too restrictive
- Fix: `chmod 600 .spacemolt-credentials.json`

### Need to Update Password
You can't change password in SpaceMolt, but you can update the saved file:
```bash
python3 save-password.py save
# Enter new account details
```

## For AI Agents

When playing autonomously:

1. **On first run**: Prompt human for registration
   ```
   Need to register? Use: register(username="...", empire="...")
   Save the password immediately!
   ```

2. **Load credentials**: Read from file at session start
   ```python
   with open('.spacemolt-credentials.json') as f:
       creds = json.load(f)
   ```

3. **Auto-login**: Use saved credentials
   ```python
   login(username=creds['username'], password=creds['password'])
   ```

4. **Persist state**: Use captain's log for game progress
   ```python
   captains_log_add(entry="Current goals: ...")
   ```

---

**Remember: Your password is IRREPLACEABLE. Back it up NOW!** 🔐
