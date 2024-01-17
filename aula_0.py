# o que é python?
# é uma linguagem de programação com as seguintes

from sys import platform


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
elif platform == "darwin":
    requisitos = "não faço ideia e está fora do escopo desse curso"
elif platform == "linux":
    requisitos = None  # já vai estar instalado 😄
else:
    raise NotImplementedError("caso específico demais")

referencias = ["https://learn.microsoft.com/en-us/windows/wsl/install"]
