# instalando git
comando = "sudo apt install git"

# principais comandos do git: basta rodar git que ele printa os comandos principais
# essa é a API do git
o_que_eh_uma_API = "Application Programming Interface: basicamente qualquer tipo de interface que permita a comunicação entre diferentes programas ou componentes"
pode_ser = [
    "web",  # por meio de requisições HTTP, é provavelmente o mais comum e quase sinônimo de API num contexto mais geral
    "CLI",  # Command Line Interface, no caso, a API do Git é CLI
    "lib/framework",  # não muito óbvio, mas a forma como usamos libs e frameworks é uma interface de programação e, portanto, uma API
    ...,
]

# configurando git
# atribuindo nome e email:
nome = input("Seu nome completo: ")
email = input("Seu e-mail: ")
comandos = [
    f"git config user.name = {nome}",
    f"git config user.email = {email}",
]

# exercício/exemplo de fluxo de trabalho a partir de um repositório local
# bônus se fizer sem usar o mouse, usando apenas o terminal
parte_0 = [
    "criar uma pasta hello_world em $HOME/dev",
    "iniciar um repositório git nessa pasta",
    "criar um arquivo main.py na pasta hello_world",
    "criar um commit com o arquivo criado com a mensagem: 'meu primeiro commit'",
]

# usando o REPL do python
o_que_eh_um_REPL = "Read Evaluate Print Loop, basicamente é como um shell interativo: você fornece inputs, que são lidos, avalidados e devolvidos para o usuário"
como_usar = "basta digitar python/python3 no terminal, que ele abrirá um shell python do tipo REPL"

# funçôes bultins que ajudam no REPL
interessantes_para_o_REPL = [
    "globals",
    "locals",
    "type",
    "dir",
]

REPL_mais_poderoso = "ipython"

# clonando um repo
endereco = input("Endereço do repo no github: ")
comando = f"git clone https://github.com/{endereco}"
