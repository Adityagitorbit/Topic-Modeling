import pdfplumber

def extract_text_from_pdf(file):
    """
    Extracts text from a given PDF file.

    Args:
        file: The PDF file object.

    Returns:
        str: Extracted text from the PDF as a single string.
    """
    text = ""  # Initialize an empty string to store extracted text

    with pdfplumber.open(file) as pdf:  # Open the PDF file
        for page in pdf.pages:  # Iterate through each page in the PDF
            page_text = page.extract_text()  # Extract text from the current page
            if page_text:  # Ensure extracted text is not None
                text += page_text + "\n"  # Append the text to the final output, adding a newline

    return text.strip()  # Return the extracted text after removing leading/trailing whitespace
