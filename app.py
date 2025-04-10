import streamlit as st
import anthropic
import os

# Configurar la página
st.set_page_config(page_title="Chat con Claude", page_icon="🤖")

# Sidebar para la clave API y selección de modelo
st.sidebar.title("Configuración")
#api_key = st.sidebar.text_input("🔑 Clave API de Anthropic", type="password")
api_key = os.getenv("ANTHROPIC_API_KEY")

model = st.sidebar.selectbox(
    "🤖 Modelo Claude",
    options=["claude-3-7-sonnet-20250219", "claude-3-opus-20240229", "claude-3-sonnet-20240229", "claude-3-haiku-20240307"],
    index=0  # por defecto: Sonnet
)

# Inicializar historial de mensajes si no existe
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("💬 Chat con Claude (Anthropic)")

# Mostrar historial de chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Entrada del usuario
if prompt := st.chat_input("Escribe tu mensaje..."):
    # Mostrar mensaje del usuario
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    if not api_key:
        st.error("⚠️ Clave incorrecta. Debes ingresar tu clave API.")
    else:
        try:
            client = anthropic.Anthropic(api_key=api_key)

            # Enviar conversación completa
            with st.spinner("Claude está pensando..."):
                response = client.messages.create(
                    model=model,
                    max_tokens=1024,
                    messages=[
                        {"role": m["role"], "content": m["content"]} for m in st.session_state.messages
                    ]
                )

            # Obtener respuesta
            answer = response.content[0].text

            # Mostrar respuesta
            with st.chat_message("assistant"):
                st.markdown(answer)

            # Guardar en historial
            st.session_state.messages.append({"role": "assistant", "content": answer})

        except Exception as e:
            st.error(f"❌ Error al llamar a la API: {e}")

