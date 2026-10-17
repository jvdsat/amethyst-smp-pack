read -p "Enter Modrinth Mod to UPDATE: " mod
cd ..
cd packwiz
packwiz update $mod
cd ..
$PWD/.venv/Scripts/python.exe $PWD/scripts/generate-modlist.py