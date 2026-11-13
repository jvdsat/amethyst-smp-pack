# Amethyst SMP Modlist
This project contains the modlist files for the Amethyst SMP.

This server is meant to be pretty chill. There's keep inventory and many powerful items making gearing up easier.

## KNOWN ISSUES
DO NOT PLACE BACKPACKS WITH EFFORTLESS BUILDING - THE BACKPACK CONTENTS WILL BE DELETED. (this is recoverable if it does occur, but requires me to restore it for you)

# Prerequisites
1. Java JRE. Suggestion: Windows install command for Java JRE from Eclipse in Command Prompt:
```bash
winget install EclipseAdoptium.Temurin.21.JRE
```
2. Whitelist yourself on this [Google Form](https://docs.google.com/forms/d/e/1FAIpQLSdoCBcKFSYoIytfGUFq6z5je2Ee2NhS0q0q0RN6ZmQhWYP8Tg/viewform?usp=sharing&ouid=100027547836001925957)

Minimum Specs: (my laptop - 2 chunk render distance on 40 fps)
- Intel 13th Gen i5-1335U (laptop)
- Iris Xe Graphics
- 5120 MB RAM

Recommended Specs:
- Modern Intel i5 or AMD Ryzen 5
- Dedicated graphics
- 6144 to 8192 MB RAM

# SETUP GUIDE
### 1. Download the packwiz installer bootstrap jar at https://github.com/packwiz/packwiz-installer-bootstrap/releases/tag/v0.0.3 
### 2. I highly recommend MultiMC or PrismLauncher as they can automatically update your mods. Otherwise you can manually update your modlist.
### 2a. Create a Minecraft 1.21.1 with NeoForge 21.1.256 instance

### 3. If your minecraft folder has a "mods" folder, place the "packwiz-installer-bootstrap.jar" file next to it: (NOT inside the mods folder)
Example: ...\instances\1.21.1\minecraft
  - cache
  - config
  - coremods
  - debug
  - downloads
  - logs
  - **mods**
  - **packwiz-installer-bootstrap.jar**
  - resourcepacks
  - saves
  - icon.png
  - options.txt
  - servers.dat
  - etc...

### From here, go to the section depending on your install

### 4a. For MultiMC, PrismLauncher, and ATLauncher:
Use this command as a pre-launch command:
```java
"$INST_JAVA" -jar "$INST_MC_DIR/packwiz-installer-bootstrap.jar" -s client https://raw.githubusercontent.com/jvdsat/amethyst-smp-pack/main/packwiz/pack.toml
```

### 4b. Manual sync with other launchers:
Run the packwiz-installer-bootstrap.jar file to update the mods in the 'mods' folder:
1. Open a terminal in the minecraft folder
2. Run the manual packwiz command:

#### Manual Packwiz Command:
```java
java -jar packwiz-installer-bootstrap.jar -s client https://raw.githubusercontent.com/jvdsat/amethyst-smp-pack/main/packwiz/pack.toml
```

### 4c. Download mods to a separate folder:
If your launcher has a more complex configuration, you can download the mods inside an empty folder. (e.g. Lunar Client)
1. Create an empty folder anywhere (suggestion: create one in Downloads)
2. Place the packwiz-installer-bootstrap.jar into this folder
3. Run the manual packwiz command above
4. The program will create a "mods" folder and other packwiz related files. Open the "mods" folder and paste the mod files into your Minecraft folder.
  - ...\Downloads\amethyst-smp-pack
    - mods
    - packwiz-installer.jar
    - packwiz.json
    - packwiz-installer-bootstrap.jar

### 5. RECOMMENDED OPTIONS
1. After you launch the game once, close the game.
2. Download the 'options.txt' in this project, and overwrite the existing 'options.txt' in the main minecraft folder (next to packwiz-installer-bootstrap.jar). The 'options.txt' in this project has recommended keybinds, volume, settings, etc.

### 6. Finish
- You should be ready to go. Launch your instance.
- Optional: After launching for the first time, overwrite the existing 'options.txt' with the one in this project.
- Check out the FAQ.

# Player Guide

Once on the server, you should be aware of the following:

MKT Essentials
1. Once you have a small base, create a 'home' with /home that you can teleport back to
2. Use /rtp to move around the map randomly to explore new areas
3. Send and accept teleport requests to players with /tpa and /tphere

Claims
1. Claim chunks as your own to prevent player and creeper griefing
2. Open Xaero's minimap with 'M', right click a chunk, and 'Claim Selected'

Exploring
- Make use of explorer's compass and nature compass to find structures and biomes easier

<br>

# General Guidelines
- Please make any long term base within roughly 2k blocks of spawn

# BACKGROUND
The modlist is meant to be updated and changed. It may also include mods whose creators do not allow them to be included in a modpack. Thus, no modpack is provided. Such a modpack would become outdated quickly and would go against mod creator licenses.

This modlist utilizes "packwiz", a .jar program which updates your local modlist with this repository. The server also syncs with this repository using packwiz, keeping your Minecraft modlist and the server in sync.

Packwiz only manages mods to sync with the server. Your personal mods and other files will not be deleted and/or edited.

The following Minecraft launchers support pre-launch commands, and thus can call the packwiz program automatically on startup, keeping your modlist automatically updated every time you launch Minecraft:
- MultiMC
- PrismLauncher
- ATLauncher

Launchers such as CurseForge, Modrinth, Lunar Client, and Badlion Client do not support pre-launch commands. Thus, the packwiz program cannot automatically keep your modlist updated on launch. If you prefer to use these launchers, you will need to run the java command yourself to keep your modlist updated.
