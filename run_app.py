import os
import sys

# Find app.py location for EXE
if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS # type: ignore
    app_path = os.path.join(base_path, "app.py")
else:
    app_path = "app.py"

os.system(f'streamlit run "{app_path}"')