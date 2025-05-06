# README - Gerenciador de Projetos VSCode  

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)  
![License](https://img.shields.io/badge/License-MIT-green.svg)  
![Maintained](https://img.shields.io/badge/Maintained%3F-Yes-brightgreen.svg)  

Um assistente Python que abre seus projetos no **VSCode** de forma organizada, com uma interface simples no terminal.  

✨ **Desenvolvido com a ajuda do DeepSeek Chat** ❤️  

---

## 🔥 Funcionalidades  

✔️ **Lista projetos** de um arquivo `caminhos.json`  
✔️ **Abre múltiplas pastas** no VSCode com um clique  
✔️ **Verifica se os caminhos existem** antes de abrir  
✔️ **Roda em segundo plano** (`.pyw`) ou no terminal (`.py`)  
✔️ **Fácil de personalizar** – edite o JSON e pronto!  

---

## 📥 Instalação e Uso  

### 1️⃣ **Baixe o projeto**  
Coloque esses arquivos em uma pasta:  
- [`gerenciador_projetos.pyw`](#) *(o programa principal)*  
- [`caminhos.json`](#) *(configure seus projetos aqui)*  

### 2️⃣ **Configure o `caminhos.json`**  
Exemplo:  
```json
{
    "Meu Site": {
        "paths": ["C:\\dev\\meusite\\frontend", "C:\\dev\\meusite\\backend"]
    },
    "IA Project": {
        "paths": ["D:\\projetos\\ia\\notebooks", "D:\\projetos\\ia\\scripts"]
    }
}
```

### 3️⃣ **Execute!**  
- **Método 1** (Terminal normal):  
  ```sh
  python gerenciador_projetos.py
  ```
- **Método 2** (Sem janela do Python, só CMD):  
  ```sh
  pythonw gerenciador_projetos.pyw
  ```
  *(Ideal para atalhos no Windows!)*  

---

## 🖼️ Preview  

```
=== Abridor de Projetos no VSCode ===  

Projetos disponíveis:  
1- Meu Site  
2- IA Project  
0- Sair  

Digite o número do projeto que deseja abrir: 1  

Abrindo projeto 'Meu Site' no VSCode...  
  Executando: code "C:\dev\meusite\frontend"  
  Executando: code "C:\dev\meusite\backend"  
```

---

## ⚙️ Personalização  

🔹 **Mude o comando do editor** (ex: `"code"` para `"subl"` se usar Sublime Text)  
🔹 **Adicione atalho no Windows** (botão direito > Enviar para > Atalho)  
🔹 **Edite cores do terminal** (modifique `os.system('color XX')`)  

---

## ❓ FAQ  

❔ **Como fechar o terminal depois?**  
➡️ Aperte `Enter` ou modifique o código para fechar automaticamente.  

❔ **Posso usar outro editor que não seja o VSCode?**  
➡️ Sim! Troque `code` no script por `subl`, `notepad++`, etc.  

---

## 📜 Licença  

MIT License - Fique à vontade para usar e modificar!  

---

💡 **Dica:** Crie um atalho na área de trabalho para o `.pyw` e organize seus projetos sem esforço!  

**Agradecimentos especiais ao DeepSeek Chat por ajudar a tornar esse projeto realidade!** 😊🚀