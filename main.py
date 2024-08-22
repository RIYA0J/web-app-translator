#
# import streamlit as st
# from googletrans import Translator
# from PyPDF2 import PdfReader
# import io
#
# # Initialize the translator
# translator = Translator()
#
# # Supported languages
# LANGUAGES = {
#     'af': 'Afrikaans',
#     'sq': 'Albanian',
#     'am': 'Amharic',
#     'ar': 'Arabic',
#     'hy': 'Armenian',
#     'az': 'Azerbaijani',
#     'eu': 'Basque',
#     'be': 'Belarusian',
#     'bn': 'Bengali',
#     'bs': 'Bosnian',
#     'bg': 'Bulgarian',
#     'ca': 'Catalan',
#     'ceb': 'Cebuano',
#     'ny': 'Chichewa',
#     'zh-cn': 'Chinese (Simplified)',
#     'zh-tw': 'Chinese (Traditional)',
#     'co': 'Corsican',
#     'hr': 'Croatian',
#     'cs': 'Czech',
#     'da': 'Danish',
#     'nl': 'Dutch',
#     'en': 'English',
#     'eo': 'Esperanto',
#     'et': 'Estonian',
#     'tl': 'Filipino',
#     'fi': 'Finnish',
#     'fr': 'French',
#     'fy': 'Frisian',
#     'gl': 'Galician',
#     'ka': 'Georgian',
#     'de': 'German',
#     'el': 'Greek',
#     'gu': 'Gujarati',
#     'ht': 'Haitian Creole',
#     'ha': 'Hausa',
#     'haw': 'Hawaiian',
#     'iw': 'Hebrew',
#     'hi': 'Hindi',
#     'hmn': 'Hmong',
#     'hu': 'Hungarian',
#     'is': 'Icelandic',
#     'ig': 'Igbo',
#     'id': 'Indonesian',
#     'ga': 'Irish',
#     'it': 'Italian',
#     'ja': 'Japanese',
#     'jw': 'Javanese',
#     'kn': 'Kannada',
#     'kk': 'Kazakh',
#     'km': 'Khmer',
#     'ko': 'Korean',
#     'ku': 'Kurdish (Kurmanji)',
#     'ky': 'Kyrgyz',
#     'lo': 'Lao',
#     'la': 'Latin',
#     'lv': 'Latvian',
#     'lt': 'Lithuanian',
#     'lb': 'Luxembourgish',
#     'mk': 'Macedonian',
#     'mg': 'Malagasy',
#     'ms': 'Malay',
#     'ml': 'Malayalam',
#     'mt': 'Maltese',
#     'mi': 'Maori',
#     'mr': 'Marathi',
#     'mn': 'Mongolian',
#     'my': 'Myanmar (Burmese)',
#     'ne': 'Nepali',
#     'no': 'Norwegian',
#     'or': 'Odia',
#     'ps': 'Pashto',
#     'fa': 'Persian',
#     'pl': 'Polish',
#     'pt': 'Portuguese',
#     'pa': 'Punjabi',
#     'ro': 'Romanian',
#     'ru': 'Russian',
#     'sm': 'Samoan',
#     'gd': 'Scots Gaelic',
#     'sr': 'Serbian',
#     'st': 'Sesotho',
#     'sn': 'Shona',
#     'sd': 'Sindhi',
#     'si': 'Sinhala',
#     'sk': 'Slovak',
#     'sl': 'Slovenian',
#     'so': 'Somali',
#     'es': 'Spanish',
#     'su': 'Sundanese',
#     'sw': 'Swahili',
#     'sv': 'Swedish',
#     'tg': 'Tajik',
#     'ta': 'Tamil',
#     'te': 'Telugu',
#     'th': 'Thai',
#     'tr': 'Turkish',
#     'uk': 'Ukrainian',
#     'ur': 'Urdu',
#     'ug': 'Uyghur',
#     'uz': 'Uzbek',
#     'vi': 'Vietnamese',
#     'cy': 'Welsh',
#     'xh': 'Xhosa',
#     'yi': 'Yiddish',
#     'yo': 'Yoruba',
#     'zu': 'Zulu'
# }
#
# def extract_text_from_pdf(file):
#     pdf_reader = PdfReader(file)
#     text = ""
#     for page in pdf_reader.pages:
#         text += page.extract_text()
#     return text
#
# def translate_text(text, dest_language):
#     return translator.translate(text, dest=dest_language).text
#
# def translate_markdown(markdown_text, dest_language):
#     lines = markdown_text.split('\n')
#     translated_lines = []
#     for line in lines:
#         if line.strip() == '':
#             translated_lines.append('')
#         else:
#             translated = translator.translate(line, dest=dest_language).text
#             translated_lines.append(translated)
#     return '\n'.join(translated_lines)
#
# def main():
#     st.set_page_config(page_title="Markdown Translator", layout="wide")
#     st.title("📄 Markdown Translator")
#
#     col1, col2 = st.columns(2)
#
#     with st.sidebar:
#         st.header("Upload Document")
#         uploaded_file = st.file_uploader("Choose a Markdown file", type=["md", "txt", "pdf"])
#
#         target_language = st.selectbox(
#             "Select target language",
#             options=list(LANGUAGES.values()),
#             index=list(LANGUAGES.values()).index("Spanish")
#         )
#
#         if uploaded_file is not None:
#             file_details = {
#                 "filename": uploaded_file.name,
#                 "filetype": uploaded_file.type,
#                 "filesize": uploaded_file.size
#             }
#             st.write(file_details)
#
#             if st.button("Translate"):
#                 if uploaded_file.type == "application/pdf":
#                     raw_text = extract_text_from_pdf(uploaded_file)
#                 else:
#                     raw_text = uploaded_file.read().decode("utf-8")
#
#                 with st.spinner("Translating..."):
#                     dest_code = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(target_language)]
#                     translated_text = translate_markdown(raw_text, dest_code)
#
#                 col1.subheader("Original Content")
#                 col1.markdown(raw_text)
#
#                 col2.subheader("Translated Content")
#                 col2.markdown(translated_text)
#
#                 translated_bytes = translated_text.encode('utf-8')
#                 st.download_button(
#                     label="Download Translated Markdown",
#                     data=translated_bytes,
#                     file_name=f"translated_{uploaded_file.name}",
#                     mime="text/markdown"
#                 )
#
#     with st.expander("🔤 Real-Time Translation"):
#         st.subheader("Type text below for instant translation")
#
#         text_to_translate = st.text_area("Enter text here...")
#         if text_to_translate:
#             dest_code = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(target_language)]
#             translated_text = translate_text(text_to_translate, dest_code)
#             st.subheader("Translated Text")
#             st.write(translated_text)
#
# if __name__ == "__main__":
#     main()
import streamlit as st
from googletrans import Translator
from PyPDF2 import PdfReader

# Initialize the translator
translator = Translator()

# Supported languages
LANGUAGES = {
    'af': 'Afrikaans',
    'sq': 'Albanian',
    'am': 'Amharic',
    'ar': 'Arabic',
    'hy': 'Armenian',
    'az': 'Azerbaijani',
    'eu': 'Basque',
    'be': 'Belarusian',
    'bn': 'Bengali',
    'bs': 'Bosnian',
    'bg': 'Bulgarian',
    'ca': 'Catalan',
    'ceb': 'Cebuano',
    'ny': 'Chichewa',
    'zh-cn': 'Chinese (Simplified)',
    'zh-tw': 'Chinese (Traditional)',
    'co': 'Corsican',
    'hr': 'Croatian',
    'cs': 'Czech',
    'da': 'Danish',
    'nl': 'Dutch',
    'en': 'English',
    'eo': 'Esperanto',
    'et': 'Estonian',
    'tl': 'Filipino',
    'fi': 'Finnish',
    'fr': 'French',
    'fy': 'Frisian',
    'gl': 'Galician',
    'ka': 'Georgian',
    'de': 'German',
    'el': 'Greek',
    'gu': 'Gujarati',
    'ht': 'Haitian Creole',
    'ha': 'Hausa',
    'haw': 'Hawaiian',
    'iw': 'Hebrew',
    'hi': 'Hindi',
    'hmn': 'Hmong',
    'hu': 'Hungarian',
    'is': 'Icelandic',
    'ig': 'Igbo',
    'id': 'Indonesian',
    'ga': 'Irish',
    'it': 'Italian',
    'ja': 'Japanese',
    'jw': 'Javanese',
    'kn': 'Kannada',
    'kk': 'Kazakh',
    'km': 'Khmer',
    'ko': 'Korean',
    'ku': 'Kurdish (Kurmanji)',
    'ky': 'Kyrgyz',
    'lo': 'Lao',
    'la': 'Latin',
    'lv': 'Latvian',
    'lt': 'Lithuanian',
    'lb': 'Luxembourgish',
    'mk': 'Macedonian',
    'mg': 'Malagasy',
    'ms': 'Malay',
    'ml': 'Malayalam',
    'mt': 'Maltese',
    'mi': 'Maori',
    'mr': 'Marathi',
    'mn': 'Mongolian',
    'my': 'Myanmar (Burmese)',
    'ne': 'Nepali',
    'no': 'Norwegian',
    'or': 'Odia',
    'ps': 'Pashto',
    'fa': 'Persian',
    'pl': 'Polish',
    'pt': 'Portuguese',
    'pa': 'Punjabi',
    'ro': 'Romanian',
    'ru': 'Russian',
    'sm': 'Samoan',
    'gd': 'Scots Gaelic',
    'sr': 'Serbian',
    'st': 'Sesotho',
    'sn': 'Shona',
    'sd': 'Sindhi',
    'si': 'Sinhala',
    'sk': 'Slovak',
    'sl': 'Slovenian',
    'so': 'Somali',
    'es': 'Spanish',
    'su': 'Sundanese',
    'sw': 'Swahili',
    'sv': 'Swedish',
    'tg': 'Tajik',
    'ta': 'Tamil',
    'te': 'Telugu',
    'th': 'Thai',
    'tr': 'Turkish',
    'uk': 'Ukrainian',
    'ur': 'Urdu',
    'ug': 'Uyghur',
    'uz': 'Uzbek',
    'vi': 'Vietnamese',
    'cy': 'Welsh',
    'xh': 'Xhosa',
    'yi': 'Yiddish',
    'yo': 'Yoruba',
    'zu': 'Zulu'
}

def extract_text_from_pdf(file):
    pdf_reader = PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def translate_text(text, dest_language):
    return translator.translate(text, dest=dest_language).text

def translate_markdown(markdown_text, dest_language):
    lines = markdown_text.split('\n')
    translated_lines = []
    for line in lines:
        if line.strip() == '':
            translated_lines.append('')
        else:
            translated = translator.translate(line, dest=dest_language).text
            translated_lines.append(translated)
    return '\n'.join(translated_lines)

def main():
    st.set_page_config(page_title="Markdown Translator", layout="wide")
    st.title("📄 Markdown Translator")

    col1, col2 = st.columns(2)

    with st.sidebar:
        st.header("Upload Document")
        uploaded_file = st.file_uploader("Choose a Markdown file", type=["md", "txt", "pdf"])

        target_language = st.selectbox(
            "Select target language",
            options=list(LANGUAGES.values()),
            index=list(LANGUAGES.values()).index("Spanish")
        )

        if uploaded_file is not None:
            file_details = {
                "filename": uploaded_file.name,
                "filetype": uploaded_file.type,
                "filesize": uploaded_file.size
            }
            st.write(file_details)

            if st.button("Translate"):
                if uploaded_file.type == "application/pdf":
                    raw_text = extract_text_from_pdf(uploaded_file)
                else:
                    raw_text = uploaded_file.read().decode("utf-8")

                with st.spinner("Translating..."):
                    dest_code = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(target_language)]
                    translated_text = translate_markdown(raw_text, dest_code)

                col1.subheader("Original Content")
                col1.markdown(raw_text)

                col2.subheader("Translated Content")
                col2.markdown(translated_text)

                # Show balloons and a success message
                st.balloons()
                st.success("🎉 Translation completed successfully!")

                # Provide a download button for the translated content
                translated_bytes = translated_text.encode('utf-8')
                st.download_button(
                    label="Download Translated Markdown",
                    data=translated_bytes,
                    file_name=f"translated_{uploaded_file.name}",
                    mime="text/markdown"
                )

                # Share button (Simulated)
                st.markdown("[Share this translation](#)", unsafe_allow_html=True)

                # Snow animation as an alternative effect
                if st.button("Celebrate!"):
                    st.snow()

    with st.expander("🔤 Real-Time Translation"):
        st.subheader("Type text below for instant translation")

        text_to_translate = st.text_area("Enter text here...")
        if text_to_translate:
            dest_code = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(target_language)]
            translated_text = translate_text(text_to_translate, dest_code)
            st.subheader("Translated Text")
            st.write(translated_text)

if __name__ == "__main__":
    main()
