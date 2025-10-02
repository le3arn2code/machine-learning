# Troubleshooting Notes

## Issue 1: Python not found
- **Cause**: Ubuntu systems use `python3` instead of `python`.
- **Resolution**: Use `python3` consistently.

## Issue 2: Pip missing
- **Cause**: Minimal installs may not include pip.
- **Resolution**: Installed with `sudo apt install python3-pip`.

## Issue 3: Virtual environment activation fails
- **Cause**: Wrong activation command used.
- **Resolution**: On Ubuntu/Linux/macOS, use `source myenv/bin/activate`. On Windows, use `myenv\Scripts\activate`.

## Issue 4: Outdated pip causing installation errors
- **Cause**: Old pip version unable to fetch wheels.
- **Resolution**: Run `python3 -m pip install --upgrade pip` inside venv.

## Final Working Commands
```bash
sudo apt update
sudo apt install -y python3 python3-pip
sudo apt install -y python3-venv
mkdir ~/ml-lab02 && cd ~/ml-lab02
python3 -m venv myenv
source myenv/bin/activate
pip install numpy pandas scikit-learn
```
