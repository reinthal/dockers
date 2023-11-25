#!/bin/bash
set +a
source .env
set -a

# create the data folder if it doesnt exist
mkdir -p "${MEDIA_FOLDER}"

# Create subdirectories for Lidarr
mkdir -p "${APP_DATA}/lidarr"

# Create subdirectories for Readarr
mkdir -p "${APP_DATA}/readarr"

# Create subdirectories for Radarr
mkdir -p "${APP_DATA}/radarr"

# Create subdirectories for Sonarr
mkdir -p "${APP_DATA}/sonarr"

# Create subdirectories for Bazarr
mkdir -p "${APP_DATA}/bazarr"

# Create subdirectories for qBittorrent
mkdir -p "${APP_DATA}/qbittorrent"

# Create subdirectories for Nginx Proxy Manager
mkdir -p "${APP_DATA}/npm/data"
mkdir -p "${APP_DATA}/npm/lencr"

# Create subdirectories for Prowlarr
mkdir -p "${APP_DATA}/prowlarr"

# Create subdirectories for Overseerr
mkdir -p "${APP_DATA}/overseerr"

echo "Subdirectories created successfully!"

