import streamlit as st
from groq import Groq

# Setup API Key (Dapatkan gratis di console.groq.com)
client = Groq(api_key="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")

st.set_page_config(page_title="Product Validator AI", layout="centered")

st.title("🚀 AI Product Market Validator")
st.write("Cek apakah ide produk digitalmu bakal laku atau malah layu.")

# Form Input
with st.form("validator_form"):
    product_name = st.text_input("Nama Produk Digital")
    description = st.text_area("Deskripsi Singkat Produk")
    target_market = st.text_input("Siapa Target Marketnya? (Contoh: Mahasiswa akhir, Pemilik UMKM)")
    price = st.number_input("Rencana Harga Produk (dalam Rupiah)", min_value=0, step=10000)
    
    submitted = st.form_submit_button("Analisis Kelayakan")

if submitted:
    # System Prompt: Ini adalah 'instruksi rahasia' agar AI jadi pakar bisnis
    prompt = f"""
    Bertindaklah sebagai Konsultan Bisnis Digital Senior. Analisis ide produk berikut:
    Nama Produk: {product_name}
    Deskripsi: {description}
    Target Market: {target_market}
    Harga: Rp{price:,}

    Tugasmu:
    1. Berikan status: [LAYAK] atau [TIDAK LAYAK].
    2. Nilai berdasarkan potensi market size dan daya beli target market tersebut terhadap harga.
    3. Jika LAYAK: Berikan 3 rekomendasi Nilai Tambah (Value-Add) agar harga bisa naik, dan 1 ide Produk Upsell.
    4. Jika TIDAK LAYAK: Berikan alasan logis kenapa tidak layak dan 2 saran perbaikan konkrit.
    
    Gunakan bahasa yang santai, profesional, dan mudah dimengerti.
    """

    with st.spinner("Sedang menghitung potensi cuan..."):
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile", # Model gratis dan cepat
        )
        response = chat_completion.choices[0].message.content
        st.markdown("---")
        st.markdown(response)