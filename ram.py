import gc
import os
import subprocess
import psutil
from flask import jsonify

def get_ram_metrics():
    ram = psutil.virtual_memory()
    return {
        "usage": ram.percent,
        "total": round(ram.total / (1024 ** 3), 2),
        "free": round(ram.available / (1024 ** 3), 2),
    }

def get_rammap_path():
    """Returns the full path to RAMMap.exe inside the lib folder."""
    # Get the current directory where the script is running
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the path to the 'lib' folder where RAMMap.exe is stored
    rammap_path = os.path.join(current_dir, 'lib', 'RAMMap.exe')
    
    return rammap_path

def clear_cache_mem():
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the path to the 'lib' folder where RAMMap.exe is stored
    rammap_path = os.path.join(current_dir, 'lib', 'RAMMap.exe')
    
    
    if os.path.exists(rammap_path):
            try:
                # Run the RAMMap command to clear the standby list
                subprocess.run([rammap_path, '-Et'], check=True)
                print("Standby list cleared successfully!")
            except subprocess.CalledProcessError as e:
                print(f"Error clearing standby list: {e}")
            else:
                print("RAMMap executable not found at the specified path.")    

        
