# 🐍 Python + VS Code Setup

> **Time needed**: 15 minutes
> **Why**: You'll write Python for Lambda functions, Streamlit apps, and AWS automation. VS Code is the editor we'll use.

---

## 1. Install Python (3.10 or newer)

### macOS

Python 3 usually comes pre-installed. Confirm:

```bash
python3 --version
# Python 3.11.x or similar
```

If it's older than 3.10, install fresh from [python.org/downloads](https://www.python.org/downloads/) or via Homebrew:

```bash
brew install python
```

### Windows

1. Download from [python.org/downloads](https://www.python.org/downloads/)
2. Run the installer
3. ⚠️ **TICK "Add Python to PATH"** at the bottom of the first screen — this is critical
4. Click **Install Now**
5. Verify in a new Terminal/PowerShell:

```bash
python --version
# Python 3.11.x or similar
```

### Linux (Ubuntu)

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv
python3 --version
```

---

## 2. Install pip + virtual environments

`pip` is Python's package installer. `venv` is the tool for isolated environments per project.

### Confirm pip works

```bash
pip --version
# or:
pip3 --version
```

If "command not found", reinstall Python with the "Add to PATH" option ticked.

### Create your first venv (we'll use this in Week 4)

```bash
mkdir ~/cloud-work
cd ~/cloud-work
python -m venv venv
```

This creates a `venv/` folder. To "enter" the environment:

```bash
# macOS/Linux:
source venv/bin/activate

# Windows (Git Bash):
source venv/Scripts/activate

# Windows (PowerShell):
.\venv\Scripts\Activate.ps1
```

Your prompt should now show `(venv)` at the start. To exit: `deactivate`.

---

## 3. Install VS Code

VS Code is Microsoft's free code editor. It works on every OS and has the best Python support.

- Download from [code.visualstudio.com](https://code.visualstudio.com/)
- Install with all defaults

### Open VS Code and verify

```bash
code --version
# 1.x.x
```

If `code` command isn't found:
- **macOS**: Open VS Code → Cmd+Shift+P → type "shell command" → click "Install 'code' command in PATH"
- **Windows**: Reinstall with "Add to PATH" option ticked

---

## 4. Essential VS Code extensions

Open VS Code → Extensions panel (Cmd+Shift+X / Ctrl+Shift+X) and install:

| Extension | Why |
|-----------|-----|
| **Python** (by Microsoft) | Syntax highlighting, IntelliSense, debugger |
| **Pylance** | Smart type checking |
| **AWS Toolkit** | Browse AWS resources, write Lambda code |
| **GitLens** | See git history in the editor |
| **Prettier** | Auto-format code on save |
| **Markdown All in One** | Better Markdown editing |

Optional but lovely:
- **One Dark Pro** (theme — easier on the eyes for long sessions)
- **Material Icon Theme** (folder icons that match file types)

---

## 5. Install the AWS CLI

You'll use this to authenticate from your laptop to AWS.

### macOS

```bash
curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
sudo installer -pkg AWSCLIV2.pkg -target /
aws --version
```

### Windows

Download the [AWS CLI MSI installer](https://awscli.amazonaws.com/AWSCLIV2.msi) and run it.

### Linux

```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
aws --version
```

### Configure AWS CLI

```bash
aws configure
```

It'll ask for:
- AWS Access Key ID: (we'll create one in Week 1 — for now, just press Enter)
- AWS Secret Access Key: (Enter)
- Default region: `eu-west-1` (or whatever you picked)
- Default output format: `json`

Don't worry about the keys for now. We'll create an IAM user with proper credentials during Week 1.

---

## 6. Install Python libraries we'll use

In your venv (the one you created in step 2):

```bash
pip install boto3 streamlit pandas Pillow plotly
```

This pre-installs everything we'll use across the bootcamp. About 50 MB total.

---

## 🚦 60-second smoke test

Open a fresh terminal and run all four:

```bash
python --version       # should show Python 3.10 or newer
git --version          # should show git version 2.x or newer
aws --version          # should show aws-cli/2.x
code --version         # should show VS Code version
```

If all four return a version: ✅ **you're ready for Week 1.**

If any fails:
- Restart your terminal — sometimes PATH changes don't take effect until reopen
- Restart your computer — for stubborn cases
- Re-check the "Add to PATH" tick (Windows)
- Post in WhatsApp with a screenshot

---

## 💡 Pro tips for VS Code

### Open a folder as a project

`File → Open Folder → choose your cloud-work folder`. VS Code remembers the layout, opened files, terminal, etc. for that project.

### Use the built-in terminal

`Ctrl + ~` (or `Cmd + ~` on Mac) opens a terminal pane right inside VS Code. Way better than alt-tabbing.

### Activate the right Python interpreter

When you open a Python file, VS Code asks "which Python interpreter?". **Choose the one from your venv** (it'll have `venv` in the path).

---

## ✅ You're done when...

- [ ] `python --version` returns 3.10 or newer
- [ ] `pip --version` works
- [ ] `code --version` works
- [ ] `aws --version` works
- [ ] You can create a venv and activate it
- [ ] VS Code has the Python + AWS Toolkit extensions installed

You now have a professional cloud development environment. Welcome to the team. ⚡

---

⬅️ [Back to Start Here](./README.md)
