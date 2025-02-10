import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image
import streamlit as st

st.set_page_config(page_title="Classificação de Cachorros e Gatos 🐶🐱")

st.title("Classificação de Cachorros e Gatos 🐶🐱")
st.write("Envie uma imagem para que o modelo classifique se é um **cachorro** ou um **gato**.")

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

@st.cache_resource  
def load_model():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = models.resnet18(weights=None)
    num_ftrs = model.fc.in_features
    model.fc = nn.Linear(num_ftrs, 2)
    model.load_state_dict(torch.load("modelo_dogs_vs_cats.pth", map_location=device))
    model.to(device)
    model.eval()
    return model, device

model, device = load_model()

def predict_image(image):
    image = Image.open(image).convert("RGB")
    image = transform(image).unsqueeze(0).to(device)

    with torch.no_grad():
        output = model(image)
        probabilities = torch.nn.functional.softmax(output[0], dim=0) 
        confidence, predicted = torch.max(probabilities, 0)

    if confidence.item() < 0.7:
        return "Não tenho certeza... pode ser outro animal! 🤔"

    return "Gato 😺" if predicted.item() == 0 else "Cachorro 🐶"

uploaded_file = st.file_uploader("Escolha uma imagem...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Imagem carregada", use_container_width=True)
    st.write("Classificando...")
    
    prediction = predict_image(uploaded_file)
    
    st.success(f"Resultado: **{prediction}**")
