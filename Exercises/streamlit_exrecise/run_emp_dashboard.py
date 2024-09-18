import subprocess
from pathlib import Path #hello

if __name__ == "__main__":
    dashboard_path = Path(__file__).parent / "03_streamlit_ex.py"
    subprocess.run(f"streamlit run {dashboard_path}", shell=True)
