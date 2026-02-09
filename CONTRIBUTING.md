# Contributing to SpaceMolt Setup

This repository helps players set up and play SpaceMolt with MCP integration and secure password management.

## Repository Purpose

This is a **player setup repository**, not the SpaceMolt game itself. It provides:
- MCP server configuration templates
- Password management utilities
- Gameplay examples and documentation
- Helper scripts for setup and automation

## What You Can Contribute

### Documentation Improvements
- Fix typos or unclear instructions
- Add examples for new gameplay scenarios
- Update setup guides for new MCP clients
- Translate documentation to other languages

### Script Enhancements
- Improve password security features
- Add new automation examples
- Create helper utilities for common tasks
- Add error handling and validation

### Configuration Templates
- Add configs for new MCP clients
- Optimize existing configurations
- Add Docker/container setups

### Examples & Tutorials
- Write gameplay tutorials
- Create advanced automation scripts
- Share successful strategies (without spoilers)
- Add troubleshooting guides

## What NOT to Contribute

❌ Game modifications (this is not the game server)
❌ Exploits or cheats
❌ Actual passwords or credentials
❌ Copyrighted content
❌ Malicious code

## How to Contribute

### 1. Fork & Clone
```bash
git clone https://github.com/YourUsername/Spacemolt.git
cd Spacemolt
```

### 2. Create a Branch
```bash
git checkout -b feature/your-feature-name
```

### 3. Make Changes
- Follow existing code style
- Test your changes
- Update documentation

### 4. Test Your Changes
```bash
# Test Python scripts
python3 -m py_compile *.py

# Test shell scripts
bash -n *.sh

# Verify configs are valid JSON
python3 -m json.tool mcp-config.json
```

### 5. Commit & Push
```bash
git add .
git commit -m "Description of changes"
git push origin feature/your-feature-name
```

### 6. Create Pull Request
- Describe what you changed and why
- Reference any related issues
- Add screenshots if applicable

## Code Style

### Python
- Use Python 3.6+ compatible syntax
- Follow PEP 8 style guidelines
- Add docstrings to functions
- Handle errors gracefully

```python
def example_function(param: str) -> dict:
    """
    Brief description of what this does.
    
    Args:
        param: Description of parameter
        
    Returns:
        Description of return value
    """
    try:
        # Implementation
        return {"success": True}
    except Exception as e:
        print(f"Error: {e}")
        return {"success": False, "error": str(e)}
```

### Shell Scripts
- Use `#!/bin/bash` shebang
- Add `set -e` for error handling
- Comment complex sections
- Quote variables: `"$variable"`

```bash
#!/bin/bash
set -e

# Description of what script does
echo "Starting process..."
```

### JSON Configuration
- Use 2-space indentation
- Validate JSON syntax
- Add comments in README, not in JSON

### Markdown Documentation
- Use clear headings
- Add code blocks with syntax highlighting
- Include examples
- Keep line length reasonable (80-100 chars)

## Security Guidelines

### Password Handling
✓ Never commit actual passwords
✓ Use example/template files
✓ Add real credential files to .gitignore
✓ Set restrictive file permissions (600)

### File Security
```python
# Good: Secure file creation
with open(filepath, 'w') as f:
    json.dump(data, f)
os.chmod(filepath, 0o600)  # User read/write only

# Bad: World-readable credentials
with open(filepath, 'w') as f:
    json.dump(data, f)
# No permission restriction!
```

### Input Validation
```python
# Good: Validate input
username = input("Username: ").strip()
if not username or len(username) < 3:
    print("Invalid username")
    return

# Bad: No validation
username = input("Username: ")
# Use directly without checking!
```

## Testing

### Manual Testing
1. Test scripts on fresh clone
2. Verify all paths are correct
3. Test error handling
4. Check documentation accuracy

### Automated Testing
```bash
# Python syntax check
python3 -m py_compile *.py

# Shell script syntax check
bash -n *.sh

# JSON validation
python3 -c "import json; json.load(open('mcp-config.json'))"
```

## Documentation Standards

### README Updates
- Keep "Quick Start" section brief
- Add detailed info in separate files
- Use clear headings and structure
- Include code examples

### Code Comments
```python
# Good: Explain WHY, not WHAT
# Wait for rate limit to avoid API errors
time.sleep(12)

# Bad: State the obvious
# Sleep for 12 seconds
time.sleep(12)
```

### File Headers
```python
#!/usr/bin/env python3
"""
Brief description of file purpose.

Longer description if needed, including:
- What it does
- How to use it
- Any important notes
"""
```

## Project Structure

```
Spacemolt/
├── skill.md                   # Full game documentation (from SpaceMolt)
├── README.md                  # Main setup guide
├── QUICKSTART.md              # 5-minute setup guide
├── EXAMPLES.md                # Code examples
├── PASSWORD.md                # Password management guide
├── mcp-config.json            # MCP server config template
├── .gitignore                 # Git ignore rules
├── .spacemolt-credentials.json.example  # Credentials template
├── spacemolt-agent.py         # Main player agent
├── save-password.py           # Password manager utility
└── quickstart.sh              # Setup verification script
```

## Common Issues & Solutions

### Python Scripts Don't Run
```bash
# Make executable
chmod +x script.py

# Or run with python3
python3 script.py
```

### Git Ignores Not Working
```bash
# If files already tracked, remove them
git rm --cached .spacemolt-credentials.json

# Then they'll be ignored
git status
```

### JSON Syntax Errors
```bash
# Validate JSON
python3 -m json.tool file.json

# Common issues:
# - Trailing commas
# - Missing quotes
# - Unescaped backslashes
```

## Need Help?

### For Setup/Gameplay Help
- Read the documentation files
- Check QUICKSTART.md
- Use in-game forum
- Visit https://spacemolt.com

### For Repository Issues
- Check existing issues
- Create new issue with details
- Include error messages
- Specify your environment

### For Code Questions
- Comment on pull request
- Open discussion issue
- Be specific about what you need

## Recognition

Contributors will be:
- Listed in CONTRIBUTORS.md (if we create one)
- Credited in commit messages
- Thanked in release notes

## Game Bug Reports

If you find **game bugs** (not setup bugs):
1. Use in-game forum: `forum_create_thread(category="bugs", ...)`
2. Visit SpaceMolt website
3. This repo is for setup, not the game itself

## License & Legal

### This Repository
- Setup scripts and documentation provided as-is
- Feel free to fork and modify
- Credit appreciated but not required

### SpaceMolt Game
- Property of its creators
- See https://spacemolt.com for game terms
- Respect their intellectual property

## Code of Conduct

### Be Respectful
- Constructive feedback only
- No harassment or trolling
- Help newcomers

### Be Professional
- Clear commit messages
- Test before submitting
- Document your changes

### Be Secure
- Never commit secrets
- Follow security guidelines
- Report vulnerabilities privately

---

## Questions?

Open an issue or discussion. We're here to help!

**Happy Contributing!** 🚀
