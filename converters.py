import subprocess

class PandocDocxConverter:
    def __init__(self, input_file: str):
        self.input_file = input_file
    
    def to_html(self, output_file: str):
        """
        Convert the input DOCX file to HTML using Pandoc.
        """
        try:
            subprocess.run(['pandoc', '-f', 'docx', '-t', 'html', self.input_file, '-o', output_file], check=True)
            print(f"Successfully converted {self.input_file} to {output_file}")
        except subprocess.CalledProcessError as e:
            print(f"Error during conversion: {e}")


class SofficeDocxConverter:
    def __init__(self, input_file: str):
        self.input_file = input_file

    def to_html(self, output_file: str):
        """
        Convert the input DOCX file to HTML using LibreOffice (soffice).
        """
        try:
            subprocess.run(['soffice', '--headless', '--convert-to', 'html', self.input_file, '--outdir', output_file], check=True)
            print(f"Successfully converted {self.input_file} to {output_file}")
        except subprocess.CalledProcessError as e:
            print(f"Error during conversion: {e}")