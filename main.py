from subprocess import call

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("STARTING SCRIPT!")

    # docker exec nextcloud occ preview:pre-generate
    call(["docker", "exec nextcloud occ preview:generate-all"])

#
# docker exec nextcloud occ preview:generate-all
