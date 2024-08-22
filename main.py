import streamlit as st
import deepl
from PyPDF2 import PdfReader

def translate_text(text, target_lang, auth_key):
    translator = deepl.Translator(auth_key)
    result = translator.translate_text(text, target_lang=target_lang)
    return result.text

def extract_text_from_pdf(pdf_file):
    pdf_reader = PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() or ""
    return text

def download_button(content, filename, label="Download"):
    st.download_button(
        label=label,
        data=content,
        file_name=filename,
        mime='text/plain',
    )

def main():
    st.title("DeepL Translator Web App")

    # Input for DeepL API key
    auth_key = st.text_input("Enter your DeepL API Key", type="password")

    if auth_key:
        # Upload multiple files
        uploaded_files = st.file_uploader("Upload your Markdown or PDF files", type=['pdf', 'md'],
                                          accept_multiple_files=True)

        if uploaded_files:
            col1, col2 = st.columns(2, gap="medium")
            with col1:
                st.subheader("Uploaded Content")
                for uploaded_file in uploaded_files:
                    if uploaded_file.type == "application/pdf":
                        content = extract_text_from_pdf(uploaded_file)
                    else:
                        content = uploaded_file.read().decode("utf-8")

                    st.markdown(f"**File:** {uploaded_file.name}", unsafe_allow_html=True)
                    st.text_area("Original Content", content, height=300, key=uploaded_file.name)

            with col2:
                st.subheader("Translated Content")

                # Extensive language list including Indian languages
                languages = {
                    "Bulgarian": "BG",
                    "Chinese (Simplified)": "ZH",
                    "Czech": "CS",
                    "Danish": "DA",
                    "Dutch": "NL",
                    "English (British)": "EN-GB",
                    "English (American)": "EN-US",
                    "Estonian": "ET",
                    "Finnish": "FI",
                    "French": "FR",
                    "German": "DE",
                    "Greek": "EL",
                    "Hindi": "HI",
                    "Bengali": "BN",
                    "Tamil": "TA",
                    "Telugu": "TE",
                    "Kannada": "KN",
                    "Malayalam": "ML",
                    "Marathi": "MR",
                    "Gujarati": "GU",
                    "Hungarian": "HU",
                    "Indonesian": "ID",
                    "Italian": "IT",
                    "Japanese": "JA",
                    "Korean": "KO",
                    "Latvian": "LV",
                    "Lithuanian": "LT",
                    "Norwegian": "NO",
                    "Polish": "PL",
                    "Portuguese (Brazilian)": "PT-BR",
                    "Portuguese (European)": "PT-PT",
                    "Romanian": "RO",
                    "Russian": "RU",
                    "Slovak": "SK",
                    "Slovenian": "SL",
                    "Spanish": "ES",
                    "Swedish": "SV",
                    "Turkish": "TR",
                    "Ukrainian": "UK"
                }

                target_language_name = st.selectbox("Select target language", list(languages.keys()))
                target_language = languages[target_language_name]

                if st.button("Translate"):
                    with st.spinner("Translating..."):
                        for uploaded_file in uploaded_files:
                            if uploaded_file.type == "application/pdf":
                                content = extract_text_from_pdf(uploaded_file)
                            else:
                                content = uploaded_file.read().decode("utf-8")

                            try:
                                translated_content = translate_text(content, target_language, auth_key)

                                # Display translated content
                                st.markdown(f"**File:** {uploaded_file.name}", unsafe_allow_html=True)
                                st.text_area("Translated Content", translated_content, height=300, key=f"{uploaded_file.name}_translated")

                                # Button to download translated text
                                download_button(translated_content, f"{uploaded_file.name}_translated.txt", "Download Translated Text")

                                # Display balloons on successful translation
                                st.balloons()

                            except Exception as e:
                                st.error(f"Translation failed: {e}")

if __name__ == "__main__":
    main()
