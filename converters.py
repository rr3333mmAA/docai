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

    def to_markdown(self, output_file: str):
        """
        Convert the input DOCX file to Markdown using Pandoc.
        """
        try:
            subprocess.run(['pandoc', '-f', 'docx', '-t', 'markdown', self.input_file, '-o', output_file], check=True)
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

    def to_xml(self, output_dir: str):
        # Note: too big
        """
        Convert the input DOCX file to XML using LibreOffice (soffice).
        """
        try:
            subprocess.run(['soffice', '--headless', '--convert-to', 'xml', self.input_file, '--outdir', output_dir], check=True)
            print(f"Successfully converted {self.input_file} to {output_dir}")
        except subprocess.CalledProcessError as e:
            print(f"Error during conversion: {e}")

    def to_markdown(self, output_dir: str):
        """
        Convert the input DOCX file to Markdown using LibreOffice (soffice).
        """
        # Error: no export filter for ignore/output/sample.markdown found, aborting.
        # Error: no export filter
        try:
            subprocess.run(['soffice', '--headless', '--convert-to', 'markdown', self.input_file, '--outdir', output_dir], check=True)
            print(f"Successfully converted {self.input_file} to {output_dir}")
        except subprocess.CalledProcessError as e:
            print(f"Error during conversion: {e}")