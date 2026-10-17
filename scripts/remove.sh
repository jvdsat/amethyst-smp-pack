read -p "Enter Modrinth Mod to REMOVE: " mod
cd ..
cd packwiz
packwiz remove $mod
cd ..
$PWD/.venv/Scripts/python.exe $PWD/scripts/generate-modlist.py