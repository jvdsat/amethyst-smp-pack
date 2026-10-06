Contains the modlist for Minecraft 1.21.1 Neoforge server Amethyst SMP.

### BACKGROUND
The modlist is meant to be updated and changed. It also may contain mods which the creators do not allow their mods to be included in a modpack. Thus, no modpack is provided. Such a modpack would become outdated quickly and would go against mod creator licenses.

This modlist utilizes "packwiz", a .jar program which updates your local modlist with this repository. The server also syncs with this repository using packwiz, keeping your Minecraft modlist and the server in sync.

Packwiz only manages mods to sync with the server. Your personal mods and other files will not be deleted and/or edited.

The following Minecraft launchers support pre-launch commands, and thus are able to call the packwiz program automatically on startup, keeping your modlist automatically updated every time you launch Minecraft:
- MultiMC
- PrismLauncher
- ATLauncher

Launchers such as CurseForge, Modrinth, Lunar Client, and Badlion Client do not support pre-launch commands. Thus the packwiz program cannot automatically keep your modlist updated on launch. If you prefer to use these launchers, you will need to run the java command yourself to keep your modlist updated.

You should have Java OpenJDK 21 installed for Minecraft and packwiz.

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

### For MultiMC, PrismLauncher, and ATLauncher
Use this command as a pre-launch command:
```java
"$INST_JAVA" -jar "$INST_MC_DIR/packwiz-installer-bootstrap.jar" -s client https://raw.githubusercontent.com/jvdsat/amethyst-smp-pack/main/pack.toml
```

### For CurseForge, Modrinth, Lunar Client, Badlion Client, etc.
If your launcher has a "mods" folder, you can place the packwiz-installer-bootstrap.jar file in the minecraft directory.
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

If your launcher has a more complex configuration, you can download the mods inside an empty folder.
1. Create an empty folder anywhere (suggestion: create one in Downloads)
3. Place the packwiz-installer-bootstrap.jar into this folder
4. Run the packwiz-installer-bootstrap.jar file to manually sync with the server.
```java
java -jar packwiz-installer-bootstrap.jar -s client https://raw.githubusercontent.com/jvdsat/amethyst-smp-pack/main/pack.toml
```
5. This will create the "mods" folder and other packwiz related files. Open the "mods" folder and copy paste them into your Minecraft folder.
<br>...\Downloads\amethyst-smp-pack
    - mods
    - packwiz-installer.jar
    - packwiz.json
    - packwiz-installer-bootstrap.jar