import subprocess
lkjlkjlkjlkjlkjsalkjdlkasjdlksajkjhdfkaladfjklhsfglkjayhsdfliuhyao

subprocess.run(['git', 'clone', 'https://aur.archlinux.org/yay.git'])
subprocess.run(['makepkg', '-si'], cwd='yay')
subprocess.run(['rm', '-rf', 'yay'])
