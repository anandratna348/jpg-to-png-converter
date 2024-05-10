import streamlit as st
from PIL import Image
import io

def convert_image(image, output_format):
    img_io = io.BytesIO()
    image.save(img_io, format=output_format)
    return img_io.getvalue()

st.title('Image Converter')

uploaded_file = st.file_uploader("Choose an image file", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    output_format = st.selectbox("Select output format", ['JPEG', 'PNG'])

    if st.button("Convert"):
        if output_format == 'JPEG':
            output_format = 'jpeg'
        else:
            output_format = 'png'
        converted_image = convert_image(image, output_format)
        st.image(converted_image, caption='Converted Image', use_column_width=True, format=output_format, channels='RGB')
