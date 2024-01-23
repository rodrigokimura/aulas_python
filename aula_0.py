from sys import platform

# PARTE 0: PYTHON

# o que é python?
# é uma linguagem de programação com as seguintes
caracteristicas = [
    "fácil de aprender",
    "grande comunidade (provavelmente a segunda maior do mundo)",
    "aplicável em várias áreas: web, dados, automação, jogos, microcontroladores",
    ...,  # sim, a elipse faz parte da sintaxe do python
]

referencias = (
    "https://www.python.org/",
    "vozes da minha cabeça",
)

# onde roda python?
roda_em = {
    "computadores": {
        "MacOS",
        "GNU/Linux",
        "Windows",
    },
    "celulares": {
        "android": "se for hipster e usar Termux",
        "iOS": "provavelmente dá, mas desconheço",
    },
    "web": "usando o super recente pyscript",
    "microcontroladores": ["micropython", "circuitpython"],
}

# o que preciso pra rodar python?
if platform == "win32":  # Windows
    requisitos = [
        "wsl2",
        "Windows 10 build 19041 ou maior",
        "capacidade de virtualização",
    ]
elif platform == "darwin":  # MacOS
    requisitos = "não faço ideia e está fora do escopo desse curso"
elif platform == "linux":
    requisitos = None  # já vai estar instalado 😄
else:
    raise NotImplementedError("caso específico demais")

referencias = ["https://learn.microsoft.com/en-us/windows/wsl/install"]


# PARTE 1: LINUX

# diferença entre terminal e shell
link = "https://unix.stackexchange.com/questions/4126/what-is-the-exact-difference-between-a-terminal-a-shell-a-tty-and-a-con"
# principais comandos do linux
comandos = [
    # pastas e arquivos (filesystem)
    "ls",  # list
    "cp",  # copy
    "mv",  # move
    "pwd",  # print work directory
    "cd",  # change directory
    "mkdir",  # make directory
    "touch",  # update timestamp
    # processos
    "top",
    "env",  # environment variables
    "pstree",  # process tree
    "kill",  # send signal by PID
    "killall",  # send signal by process name
    # utilitários
    "which",  # onde está o programa usado
    "grep",  # Gnu Regular Expression Program?
]
# precisa saber disso ☝️?? sim, bem importante, pelo menos os de filesystem


# exemplos de emuladores de terminal
exemplos_terminal = [
    "gnome-terminal",  # padrão do Gnome (desktop environment)
    "konsole",  # padrão do KDE (desktop environment)
    "xterm",  # roda no X (servidor gráfico)
    "tmux",  # focado em multiplex ("tiling" no terminal)
    "allacitty",  # focado em performance
    "kitty",  # focado em performance e funcionalidades
]
# precisa saber disso ☝️?? não, mas precisa escolher um pra usar

# exemplos de emuladores de terminal
exemplos_shell = [
    "bash",  # padrão na maioria das distros
    "zsh",  # foco em funcionalidades e extensibilidade
    "fish",  # foco em simplicidade
]
# precisa saber disso ☝️?? não, mas precisa escolher um pra usar

# customizando o shell:
# é possível configurar o shell para um melhor
