import PyPDF2

def extract_pages(pdf_path, start_page, end_page, output_path):
    # Opening the original PDF
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)

        # Creating a PDF writer object
        writer = PyPDF2.PdfWriter()

        # Adding pages from the original PDF to the writer
        for i in range(start_page-1, end_page):
            writer.add_page(reader.pages[i])

        # Writing the selected pages to a new PDF
        with open(output_path, 'wb') as output_file:
            writer.write(output_file)

# Replace 'original.pdf' with the path to your PDF file
# The output will be saved as 'output.pdf'
extract_pages('2023.11.13.566791v1.full.pdf', 4, 11, 'output.pdf')

