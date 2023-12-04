import subprocess

def get_commit_hash(self):
        try:
            # Run 'git rev-parse HEAD' command to get the commit hash
            result = subprocess.run(['git', 'rev-parse', 'HEAD'], capture_output=True, text=True, check=True)
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            print(f"Error retrieving commit hash: {e}")
            return "Unknown"