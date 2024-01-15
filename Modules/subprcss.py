import subprocess
import re


def list_installed_programs():
    try:
        # Use the system profiler command to get a list of installed apps.
        result = subprocess.run(['system_profiler', 'SPApplicationsDataType'], capture_output=True, text=True)

        # Check if the command was successful
        if result.returncode == 0:
            # Split the output into lines and look for lines containing "Location:"
            lines = result.stdout.split('\n')
            for line in lines:
                if "Location:" in line:
                    # Exctract the app name from the "Location:" line
                    program_name = line.split(':', 1)[1].strip()
                    print(program_name.split('/')[-1])
        else:
            print("Error:", result.stderr)
    except Exception as e:
        print("An error occured:", e)


if __name__ == "__main__":
    list_installed_programs()