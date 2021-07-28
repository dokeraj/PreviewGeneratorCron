from subprocess import call

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("STARTING SCRIPT!")

    # docker exec nextcloud occ preview:pre-generate
    call(["docker", "exec nextcloud occ preview:generate-all"])

    import time

    print("Printed immediately.")
    time.sleep(256.4)

#
# docker exec nextcloud occ preview:generate-all
