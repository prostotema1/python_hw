def generate_latex_table(data):
    latex = "\\begin{tabular}{|" + " | ".join(["c"] * len(data[0])) + "|}\n"
    latex += "\\hline\n"

    for row in data:
        latex += " & ".join(map(str, row)) + " \\\\\n"
        latex += "\\hline\n"

    latex += "\\end{tabular}\n"
    return latex


def generate_latex_image(image_path, caption="Sample Image", label="fig:sample"):
    return "\n".join([
        "\\begin{figure}[h!]",
        "\\centering",
        f"\\includegraphics[width=0.8\\textwidth]{{{image_path}}}",
        f"\\caption{{{caption}}}",
        f"\\label{{{label}}}",
        "\\end{figure}"
    ])
