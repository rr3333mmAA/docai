from converters import PandocDocxConverter, SofficeDocxConverter

if __name__ == "__main__":
    input_file = "sample.docx"
    output_dir = "ignore/output"

    pandoc_converter = PandocDocxConverter(input_file)
    soffice_converter = SofficeDocxConverter(input_file)
    
    pandoc_converter.to_markdown(f"{output_dir}/output_pandoc.md")
    soffice_converter.to_markdown(f"{output_dir}")