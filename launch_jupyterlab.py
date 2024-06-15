########## Jupyterlab Environment 

import subprocess
import webbrowser

def launch_jupyterlab():
    try:
        # Launch JupyterLab using subprocess to run the command 'jupyter lab'
        subprocess.Popen(['jupyter', 'lab'])

        # Open the default web browser to the JupyterLab URL (http://localhost:8888)
        webbrowser.open_new_tab('http://localhost:8888/lab')
        
        print("JupyterLab has been launched. Check your web browser.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    launch_jupyterlab()

