# 🐶🐱 Classificação de Cachorros e Gatos com IA  

Este é um projeto de **classificação de imagens** que utiliza um modelo de **Deep Learning** para identificar se uma imagem contém um **cachorro** ou um **gato**. O modelo foi treinado previamente e está pronto para ser utilizado através de uma interface web simples, feita com **Streamlit**.  
Basta enviar uma imagem e o modelo retornará se é um **cachorro** ou um **gato**, com base no treinamento realizado.  

## 🛠️ Tecnologias Utilizadas  

- **Python**  
- **PyTorch** (para inferência do modelo)  
- **Torchvision** (transformações nas imagens)  
- **Streamlit** (para a interface web)

## 📦 Como Rodar o Projeto  

### 1️⃣ Clone o Repositório  

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
```

### 2️⃣ Instale as Dependências
```bash
pip install -r requirements.txt
```

### 3️⃣ Execute a Aplicação
```bash
streamlit run app.py
```

## Ou, acesso o link: https://classificador-imagens.streamlit.app

## ⚠️ Possíveis Limitações

Embora o modelo funcione bem para diferenciar cachorros e gatos, ele pode apresentar falhas em alguns casos, como:

- Se a imagem for de outro animal ou objeto, o modelo pode classificar incorretamente.
- Se a imagem estiver muito escura, cortada ou distorcida, a predição pode não ser precisa.
- O modelo não reconhece humanos corretamente e pode classificá-los como um dos animais.
