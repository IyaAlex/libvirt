#!/bin/bash
# Install libvirt deps
apk update
apk add libvirt-client polkit libvirt-dev gcc libc-dev
# Copy ssh key
cp /config/.ssh /root/ -R

