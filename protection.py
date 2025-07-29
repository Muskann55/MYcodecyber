from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.errors import PdfReadError
import sys

def create_password_protected_pdf(input_path, output_path, password):
    try:
        reader = PdfReader(input_path)
        writer = PdfWriter()

        for page in reader.pages:
            writer.add_page(page)

        writer.encrypt(password)

        with open(output_path, "wb") as f:
            writer.write(f)

        print(f"PDF '{output_path}' has been successfully encrypted.")

    except PdfReadError:
        print("Error: Failed to read the input PDF. It may be corrupted or encrypted.")
    except FileNotFoundError:
        print("Error: Input PDF file not found.")
    except Exception as e:
        print(f"Unexpected error: {e}")

def main():
    if len(sys.argv) != 4:
        print("Usage: python protection.py <input.pdf> <output.pdf> <password>")
        return

    input_pdf = sys.argv[1]
    output_pdf = sys.argv[2]
    password = sys.argv[3]

    create_password_protected_pdf(input_pdf, output_pdf, password)

if __name__ == "__main__":
    main()
