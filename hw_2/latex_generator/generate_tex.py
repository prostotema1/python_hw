from latex_generator import generate_latex_table, generate_latex_image


def generate_latex_file():
    data = [
        ["Header1", "Header2", "Header3"],
        ["Row1", "Value1", "Value2"],
        ["Row2", "Value3", "Value4"]
    ]

    table_latex = generate_latex_table(data)
    image_latex = generate_latex_image("example_image.png")

    latex_code = """
    \\documentclass{article}
    \\usepackage{graphicx}
    \\begin{document}
    \\section*{Generated Table and Image}
    """ + table_latex + image_latex + """
    \\end{document}
    """

    with open("../artifacts/generated_document.tex", "w") as f:
        f.write(latex_code)


if __name__ == "__main__":
    generate_latex_file()
