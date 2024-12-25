Libvirt client for start and shutdown VM from home-assistant

---
# Prepare home assistant
## Docker :
Open a bash in your home-assistant container
``` bash
docker exec -it [container-name] /bin/bash
```
Install dependencies
``` bash
apk update
apk add libvirt-client polkit libvirt-dev gcc libc-dev
```
Generate ssh public key
``` bash
ssh-keygen  -N "" 
cp /root/.ssh /config -R
cat /root/.ssh/id_rsa.pub
```

## Ubuntu/Debian :
``` bash
apt-get update
apt-get install libvirt-client libvirt-dev gcc
```
Generate ssh public key (for www-data user) 
``` bash
sudo -u www-data
ssh-keygen  -N "" 
cat .ssh/id_rsa.pub
```

---
# After home-assistant update container (Docker)
Open a bash in your home-assistant container
``` bash
docker exec -it [container-name] /bin/bash
```
Install dependencies
``` bash
apk update
apk add libvirt-client polkit libvirt-dev gcc libc-dev
```
Copy ssh public key
``` bash
cp /config/.ssh /root/ -R
```


---
# Allow acces on libvirt server
## Add hass user to remote libvirt server :
``` bash
useradd -G libvirt kvm -m hass
```
## Add ssh passkey :
``` bash
mkdir /home/hass/.ssh
chown hass:hass /home/hass/.ssh
echo "[content of id_ras.pub generate previously]" > /home/hass/.ssh/authorized_keys
```

---
# Add device to home-assistant
configuration.yaml
```
switch: 
  - platform: libvirt
    name: [Name of VM]
    url: [URI : example qemu+ssh://hass@192.168.1.1/system]
```

