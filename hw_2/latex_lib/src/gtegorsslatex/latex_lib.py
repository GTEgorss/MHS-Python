def generate_latex_file(file_path, data_list, has_graphics=False):
    if not data_list or not isinstance(data_list, list) or not all(isinstance(data, str) for data in data_list):
        raise ValueError("Data list must be a list of strings.")

    with open(file_path, "w", encoding="utf-8") as file:
        file.write("\\documentclass{article}\n")

        if has_graphics:
            file.write("\\usepackage{graphicx}\n")
            file.write("\\graphicspath{ {.} }\n")

        file.write("\\begin{document}\n")

        for data in data_list:
            file.write(data)
            file.write("\n")

        file.write("\\end{document}")

def generate_table(data):
    if not data or not isinstance(data, list) or not all(isinstance(row, list) for row in data):
        raise ValueError("Input must be a list of lists.")

    row_lengths = {len(row) for row in data}
    if len(row_lengths) > 1:
        raise ValueError("All rows must have the same number of elements.")

    num_columns = row_lengths.pop()

    latex_code = "\\begin{tabular}{ | " + " | ".join(["c"] * num_columns) + " | }\n\\hline\n"

    for row in data:
        row_content = " & ".join(str(cell) for cell in row)
        latex_code += f"{row_content} \\\\\n\\hline\n"

    latex_code += "\\end{tabular}"
    return latex_code

def generate_image(img_path):
    latex_code = "\\begin{figure}\n"
    latex_code += f"\\includegraphics[width=\\linewidth]{{{img_path}}}\n"
    latex_code += "\\end{figure}\n"
    return latex_code