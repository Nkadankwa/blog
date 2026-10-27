+++
title = "Part 1 — Cross-Platform Sharing and the Portable Cloud Experiment"
date = "2025-03-23T00:00:00+08:00"
recorded_period = "February 18–March 23, 2025; later recollections in May and November 2025"
weight = 2
description = "Nextcloud, Docker and external storage across several operating systems."
technical = true
+++

*Names, host addresses and other identifying values use consistent dummy examples. Exact hardware models and capacities are omitted. Commands describe this setup at the time; suggested changes are identified in the text.*

## Why a portable cloud seemed useful

Moving notes, videos, audio, and other files between devices was the practical problem behind this project. By March 10, the requirement covered Windows, Linux, macOS, Android, and iOS, with the added complication that I might move between living arrangements. An external drive seemed like a useful place to keep a setup that could travel with me.

The early experiments brought together Nextcloud, Docker Desktop, WSL, and remote-access options. YouTube and AI helped with the Docker setup, although adapting the instructions and getting Compose right became a project in itself. That combination of resources is something I described again when writing about the experience in May.

## Getting the containers started

The first problems appeared on March 12, before storage portability could really be tested. Running Compose from the drive root produced `project name must not be empty`, alongside a warning that the `version` attribute was obsolete. A later image download ended with `Unexpected eof`, so even reaching the application required several attempts.

Nextcloud eventually reached its account and database setup screen, which was a useful step forward, but access still behaved differently across devices. One browser reported an untrusted domain, while the phone would not load the service at all. Another attempt failed because something was already using the chosen host port:

```text
Bind for 0.0.0.0:8080 failed: port is already allocated
```

These errors needed separate explanations. A port collision affected whether a container could start with that binding, whereas the untrusted-domain message came from an application that had already responded to a request. Advice at the time included using an explicit Compose project name and resolving the existing port binding, but neither change on its own would establish that every device could reach Nextcloud.

### The storage configuration being compared

One Compose file being considered used these bind mounts. This is a shortened configuration fragment, with placeholder paths and passwords; it is not a complete deployment file.

```yaml
services:
  db:
    image: mariadb:10.6
    volumes:
      - /path/to/external/ssd/mariadb:/var/lib/mysql
    environment:
      MYSQL_DATABASE: nextcloud
      MYSQL_USER: nextcloud
      MYSQL_PASSWORD: EXAMPLE_DATABASE_PASSWORD

  app:
    image: nextcloud:stable
    ports:
      - "8080:80"
    volumes:
      - /path/to/external/ssd/nextcloud:/var/www/html
      - /path/to/external/ssd/nextcloud/data:/var/www/html/data
    environment:
      MYSQL_HOST: db
      MYSQL_DATABASE: nextcloud
      MYSQL_USER: nextcloud
      MYSQL_PASSWORD: EXAMPLE_DATABASE_PASSWORD
```

The left side of each mount is a host path; the right side is where the container sees it. Mounting the data directory alone would not make the whole stack portable: the database and application configuration also need to remain available. The `8080:80` entry publishes container port `80` as host port `8080`.

### Additional checks for the actual mounts

From the directory containing the Compose file, these commands would check the project and its mounts before moving data:

```bash
docker compose config --quiet
docker compose ps --all
docker inspect nextcloud-app-1 --format '{{json .Mounts}}'
docker inspect nextcloud-db-1 --format '{{json .Mounts}}'
```

The container names must match `docker ps --all`. In the mount output, compare `Type`, `Source` and `Destination` with the intended external-drive path. A named volume is different from a bind mount to that drive. The inspection establishes where Docker attached storage, while a file write and read-back test is still needed to establish usable persistence.

[`docker inspect`](https://docs.docker.com/reference/cli/docker/inspect/) describes the mount information; [`docker compose config`](https://docs.docker.com/reference/cli/docker/compose/config/) checks the configuration before startup.

## Why a running Nextcloud was not enough

The storage problem became clearer when the expected `nextcloud` directory remained empty. On March 13, the service was still running even though the external drive was disconnected, which meant the running application was not using the storage arrangement I had intended. The exact mounts still needed checking, but the application's availability was already a poor test of whether the portable setup worked.

At the same time, Nextcloud displayed another error:

```text
Cannot write into "config" directory!
```

The container listing showed `nextcloud-app-1` and `nextcloud-db-1`, but trying to shut the stack down from `C:\Users\labuser` returned `no configuration file provided: not found`. In other words, the command had been issued from a location where Compose could not find the configuration; it did not show that the intended stack had been removed.

Permissions, WSL mount settings, and directory ownership were all discussed as possible ways forward. The tests did not show that the intended external directories were receiving the application's data, so those suggestions remain part of the investigation rather than a finished storage solution.

## Storage interruptions made the investigation harder

The same period included an earlier drive that became unavailable, recovered, and then started clicking. After a cable change and reseating the board connected to the drive, the clicking reportedly stopped. That was an improvement, but it did not isolate the fault to the cable, adapter, or drive itself.

A later message on March 18 said the SSD had arrived, so the earlier clicking episode should not simply be assigned to that newer SSD. The partitioning plan then split the available space between a broadly compatible filesystem and Linux storage, with Windows showing an exFAT partition and a separate area of unallocated space.

WSL added another layer of confusion because the device listing did not match what I expected to see. One suggested device, `sdc`, turned out to be the computer's storage rather than the external SSD. By March 23, `/mnt/e` could be accessed, but Compose still was not writing to the SSD, leaving the original portability requirement unfinished.

## What this attempt taught me

The main distinction was between starting a service and proving where its data lived. Nextcloud could respond in a browser while the intended directory remained empty, and troubleshooting access did not automatically resolve the persistence problem. Shell differences also caused avoidable detours, including Windows rejecting `ls` and a literal placeholder in `docker logs <container_name>` producing a syntax error.

By March 23, Compose still was not writing to the SSD. Registry mirrors, permissions and WSL settings had all been investigated, but the portable-cloud setup remained unfinished.

The next stage moved toward a dedicated host, covered in [Part 2]({{< relref "/guides/homelab/02-proxmox-to-ubuntu.md" >}}).

{{< details summary="More command output" >}}

These excerpts include longer output from the same work. Names and identifying values have been replaced; copied terminal text may contain incomplete lines.

```text
Error response from daemon: driver failed programming external connectivity on endpoint nextcloud-portable-app-1 (a097e46c50bd8a184a23bb93949696141b9376bf64c9df9d38308e1005cea8cc): Bind for 0.0.0.0:8080 failed: port is already allocated
```

{{< /details >}}
