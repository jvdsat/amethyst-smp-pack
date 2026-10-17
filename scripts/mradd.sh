read -p "Enter Modrinth Mod to ADD: " mod
cd ..
cd packwiz
packwiz mr add $mod
cd ..
$PWD/.venv/Scripts/python.exe $PWD/scripts/generate-modlist.py