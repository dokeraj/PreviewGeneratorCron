import docker
import sys
import configInit
import time


def checkNextcloudValidity(container):
    if "nextcloud" in container.attrs["Config"]["Image"]:
        return True
    else:
        return False


def checkNextcloudAvailability(dockerClient, config):
    try:
        container = dockerClient.containers.get(config.nextcloudContainerName)
        return True, container
    except Exception as e:
        return False, None


def mainChecks():
    try:
        client = docker.DockerClient(base_url='unix://var/run/docker.sock')
    except Exception as e:
        print("ERROR: Cannot find docker server! Now exiting!")
        sys.exit(0)

    print("Reading the config from the YAML file...")
    config = configInit.initConfig()

    print("Checking the availability and validity of Nextcloud container...")
    available, container = checkNextcloudAvailability(client, config)

    if not available:
        print(
            f"WARN: The container name {config.nextcloudContainerName} is not valid or the container is stopped - trying again in 5 minutes")
        time.sleep(300)
        return mainChecks()

    if not checkNextcloudValidity(container):
        print(f"ERROR: The container with name {config.nextcloudContainerName} is not created from the nextcloud image! Please use a container that it is the Nextcloud! Now exiting!")
        sys.exit(0)

    print("SUCCESS: The specified container is currently running and is in fact Nextcloud container!")
    return container, config
