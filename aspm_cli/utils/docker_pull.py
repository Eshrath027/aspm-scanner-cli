import subprocess
import os

from aspm_cli.utils.logger import Logger

def docker_pull(image: str):
    """Pull a Docker image using subprocess, or skip if it already exists locally."""
    # # Check if image exists locally first
    # check_result = subprocess.run(
    #     ["docker", "image", "inspect", image],
    #     capture_output=True,
    #     text=True
    # )

    # if check_result.returncode == 0:
    #     print("docker image exists locally: ", image)
    #     Logger.get_logger().debug(f"Docker image already exists locally: {image}")
    #     return
    
    Logger.get_logger().info(f"Pulling Docker image: {image}")
    result = subprocess.run(["docker", "pull", image], capture_output=True, text=True)

    if result.returncode != 0:
        Logger.get_logger().error(f"Failed to pull image {image}")
        Logger.get_logger().error(result.stderr)
        raise RuntimeError(f"Failed to pull image: {image}")
    else:
        Logger.get_logger().debug(result.stdout)
        Logger.get_logger().debug(f"Successfully pulled image: {image}")