import tkinter as tk

# Função para atualizar o visor da calculadora
def atualizar_visor(valor):
    texto_atual = visor.get()
    visor.delete(0, tk.END)
    visor.insert(0, texto_atual + valor)

# Função para limpar o visor
def limpar_visor():
    visor.delete(0, tk.END)

# Função para calcular o resultado
def calcular():
    try:
        expressao = visor.get()
        resultado = str(eval(expressao))  # Avalia a expressão matemática
        visor.delete(0, tk.END)
        visor.insert(0, resultado)
    except Exception as e:
        visor.delete(0, tk.END)
        visor.insert(0, "Erro")

# Criação da janela principal
janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("300x400")
janela.configure(bg="#f0f0f0")

# Visor da calculadora
visor = tk.Entry(janela, font=("Arial", 24), justify="right", bd=10, relief=tk.FLAT)
visor.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Botões da calculadora
botoes = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
    ('=', 5, 0, 1, 4)  # Botão "=" ocupa 4 colunas
]

# Adicionando os botões à interface
for (texto, linha, coluna, *args) in botoes:
    if texto == '=':
        botao = tk.Button(janela, text=texto, font=("Arial", 18), bg="#4CAF50", fg="white", command=calcular)
        botao.grid(row=linha, column=coluna, columnspan=args[0], sticky="nsew", padx=5, pady=5)
    elif texto == 'C':
        botao = tk.Button(janela, text=texto, font=("Arial", 18), bg="#FF5733", fg="white", command=limpar_visor)
        botao.grid(row=linha, column=coluna, sticky="nsew", padx=5, pady=5)
    else:
        botao = tk.Button(janela, text=texto, font=("Arial", 18), bg="#333333", fg="white", command=lambda t=texto: atualizar_visor(t))
        botao.grid(row=linha, column=coluna, sticky="nsew", padx=5, pady=5)

# Ajustando o layout da grade
for i in range(6):
    janela.grid_rowconfigure(i, weight=1)
for j in range(4):
    janela.grid_columnconfigure(j, weight=1)

# Inicia o loop principal da interface gráfica
janela.mainloop()