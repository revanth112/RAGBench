import uuid

from pypdf import PdfReader

from models.document import Document


class DocumentService:
    @staticmethod
    def process_pdf(uploaded_file):

        reader = PdfReader(uploaded_file)

        full_text = ""

        total_pages = len(reader.pages)

        for page in reader.pages:

            text = page.extract_text()

            if text:
                full_text += text + "\n"
        document = Document(
            document_id=str(uuid.uuid4()),
            document_name=uploaded_file.name,
            total_pages=total_pages,
            raw_text=full_text
        )
        return document