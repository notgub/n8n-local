import subprocess
import os

compose_file = os.path.join(os.path.dirname(__file__), '../docker/docker-compose.yml')

def run_docker_compose_up():
    try:
        subprocess.run(
            ["docker", "compose", "-p", "n8n-local-stack", "-f", compose_file, "up", "-d"],
            check=True
        )
        print("Docker Compose started successfully with stack name 'n8n-local-stack'.")
    except subprocess.CalledProcessError as e:
        print(f"Error running Docker Compose: {e}")

if __name__ == "__main__":
    run_docker_compose_up()