Contains the modlist info for Amethyst SMP. View the list of mods from the MODLIST.md file

Download the packwiz-installer.jar and packwiz-installer-bootstrap.jar from their repositories and place them inside the minecraft/ directory.

Use the following pre-launch command to sync your local modlist with the server:
"$INST_JAVA" -jar "$INST_MC_DIR/packwiz-installer-bootstrap.jar" -s client https://raw.githubusercontent.com/jvdsat/amethyst-smp-pack/main/pack.toml
