import subprocess

packages = \
["swaybg", #Основные пакеты!
"kiity",
"waybar",
"fish",
"wofi",
"git",
"thunar",
"gtk2",
"gtk3",
"gtk4",
"neofetch",
"w3m",
"sudo pacman -S gnome-screenshot"
#Шрифты !
"ttf-dejavu",
"ttf-font-awesome",
"ttf-liberation",
"ttf-dejavu ",
"powerline-fonts",
"noto-fonts",
"ttf-fira-code",
"ttf-hack",
"terminus-font",
"adobe-source-code-pro-fonts",
"otf-font-awesome",
"ttf-jetbrains-mono",
"nerd-fonts-complete",
"ttf-fira-code-nerd",
"powerline-fonts",
"ttf-google-fonts-git",
"nerd-fonts",
"fc-cache -fv",
#--------------------
"noto-fonts-emoji",
"ttf-joypixels",
#Утилиты
"inetutils",
"pkgfile",
"base-devel",
"grim",
#Обновления
"sudo pacman -Syu"

]


for packag in  packages:
    subprocess.run(["sudo", "pacman", "-S", "--noconfirm", packag])
