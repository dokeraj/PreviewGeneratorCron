import docker
import schedule
import time
import configInit
import calendar
from datetime import datetime
import sys


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("STARTING SCRIPT!")

    # docker exec nextcloud occ preview:pre-generate

    try:
        client = docker.DockerClient(base_url='unix://var/run/docker.sock')
    except Exception as e:
        print("ERROR: cannot find docker server! now exiting!")
        sys.exit(0)

    config = configInit.initConfig()

    ## todo:: if you cannot get the container name - wait 1 minute and try again -> up to 5 times
    container = client.containers.get(config.nextcloudContainerName)
    container.exec_run(cmd="occ preview:generate-all")




