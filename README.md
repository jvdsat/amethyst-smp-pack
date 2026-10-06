### Amethyst SMP Modlist
This project contains the files for the modlist for the Amethyst SMP.

Read the Pre-requisites to see if this is even something you want to do. It's quite some setup.

## Pre-Requisites
1. Install Java OpenJDK 21
2. 6 GB RAM recommended. You can allocate more up to 8GB if you're seeing stutters. Flying at max speed with elytra was perfect at 6GB.
3. Tailscale VPN (so you can connect to my home) https://tailscale.com/
4. Minecraft 1.21.1 Neoforge 21.1.234 instance with 6144 MB RAM. Optionally, 8192 MB RAM.
5. Whitelist yourself on this [Google Form](https://docs.google.com/forms/d/e/1FAIpQLSdoCBcKFSYoIytfGUFq6z5je2Ee2NhS0q0q0RN6ZmQhWYP8Tg/viewform?usp=sharing&ouid=100027547836001925957)

### BACKGROUND
The modlist is meant to be updated and changed. It also may contain mods which the creators do not allow their mods to be included in a modpack. Thus, no modpack is provided. Such a modpack would become outdated quickly and would go against mod creator licenses.

This modlist utilizes "packwiz", a .jar program which updates your local modlist with this repository. The server also syncs with this repository using packwiz, keeping your Minecraft modlist and the server in sync.

Packwiz only manages mods to sync with the server. Your personal mods and other files will not be deleted and/or edited.

The following Minecraft launchers support pre-launch commands, and thus are able to call the packwiz program automatically on startup, keeping your modlist automatically updated every time you launch Minecraft:
- MultiMC
- PrismLauncher
- ATLauncher

Launchers such as CurseForge, Modrinth, Lunar Client, and Badlion Client do not support pre-launch commands. Thus the packwiz program cannot automatically keep your modlist updated on launch. If you prefer to use these launchers, you will need to run the java command yourself to keep your modlist updated.

## SETUP GUIDE

1. Install the packwiz installer bootstrap jar at https://github.com/packwiz/packwiz-installer-bootstrap/releases/tag/v0.0.3 
2. Place the "packwiz-installer-bootstrap.jar" file in your Minecraft folder. (NOT the mods folder)
<br>Example file structure:
<br>...\instances\1.21.1\minecraft
    - cache
    - config
    - coremods
    - debug
    - downloads
    - logs
    - mods
    - resourcepacks
    - saves
    - icon.png
    - options.txt
    - servers.dat
    - packwiz-installer-bootstrap.jar

### For MultiMC, PrismLauncher, and ATLauncher:
Use this command as a pre-launch command:
```java
"$INST_JAVA" -jar "$INST_MC_DIR/packwiz-installer-bootstrap.jar" -s client https://raw.githubusercontent.com/jvdsat/amethyst-smp-pack/main/pack.toml
```

### For installs with a "mods" folder:
If your launcher has a "mods" folder, place the packwiz-installer-bootstrap.jar file in the minecraft directory.
<br>...\instances\1.21.1\minecraft
    - cache
    - config
    - coremods
    - debug
    - downloads
    - logs
    - mods
    - packwiz-installer-bootstrap.jar

Run the packwiz-installer-bootstrap.jar file to manually sync with the server.
```java
java -jar packwiz-installer-bootstrap.jar -s client https://raw.githubusercontent.com/jvdsat/amethyst-smp-pack/main/pack.toml
```

### For installs with complex directory structure:
If your launcher has a more complex configuration, you can download the mods inside an empty folder. 
For example,the Lunar Client folder has a mods folder, then a folder for each instance. In this case you cannot use the packwiz java command, which creates a mods folder.
1. Create an empty folder anywhere (suggestion: create one in Downloads)
2. Place the packwiz-installer-bootstrap.jar into this folder
3. Run the packwiz-installer-bootstrap.jar file
```java
java -jar packwiz-installer-bootstrap.jar -s client https://raw.githubusercontent.com/jvdsat/amethyst-smp-pack/main/pack.toml
```
4. The prorgam will create a "mods" folder and other packwiz related files. Open the "mods" folder and copy paste the mod files into your Minecraft folder.
<br>...\Downloads\amethyst-smp-pack
    - mods
    - packwiz-installer.jar
    - packwiz.json
    - packwiz-installer-bootstrap.jar