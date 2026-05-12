import streamlit as st
import google.generativeai as genai

# 1. Konfigurasi API KEY
# Rahasia ini akan kita masukkan nanti di settingan Streamlit Cloud
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# 2. Judul Aplikasi di Browser
st.set_page_config(page_title="SI_ReReAI - Genre Cilegon", page_icon="👌")
st.title("SI_ReReAI 🤖")
st.caption("Asisten Virtual Edukasi Forum Genre Kota Cilegon")

# 3. "Otak" & Materi SI_ReReAI
materi_genre = """
Kamu adalah SI_ReReAI, asisten virtual ramah dari Forum Genre Cilegon. 
Berikut adalah panduan materi utama kamu:

1. PuP (Pendewasaan Usia Perkawinan): Upaya meningkatkan usia perkawinan minimal 21 thn (P) & 25 thn (L).
2. 5 Transisi Remaja: Pendidikan, Mencari pekerjaan, Memulai kehidupan berkeluarga, Menjadi anggota masyarakat, Menerapkan pola hidup sehat.
3. 8 Fungsi Keluarga: Agama, Cinta kasih, Reproduksi, Ekonomi, Sosial budaya, Perlindungan, Pendidikan, Lingkungan.
4. 4T (Terlalu): Hamil terlalu muda (<21 thn), Hamil terlalu tua (>35 thn), Terlalu banyak anak (>2), Jarak anak terlalu rapat (<3 thn).
5. Salam GenRe: Triad Genre (Hindari Seks Bebas, Narkoba, Pernikahan Dini).
6. TRIBINA: BKB (Balita), BKR (Remaja), BKL (Lansia).

Gaya bicara: Gaul khas remaja Cilegon, ramah, semangat, dan wajib akhiri dengan 'Salam GENRE! 👌'.
"""

# 4. Logika Chat
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Tanya SI_ReReAI tentang Genre..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        model = genai.GenerativeModel('gemini-1.5-flash', system_instruction=materi_genre)
        response = model.generate_content(prompt)
        st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
