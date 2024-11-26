from gtegorsslatex.latex_lib import *
import os.path
import subprocess


def generate_pdf_from_tex(tex_file_path, output_dir):
    try:
        if not os.path.isfile(tex_file_path):
            raise FileNotFoundError(f"The file {tex_file_path} does not exist.")

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        print("Started creating PDF...")
        result = subprocess.run(
            ["pdflatex", f"-output-directory={output_dir}", tex_file_path],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            print("PDF created successfully.")
        else:
            print(f"Error during pdflatex execution:\n{result.stderr}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    data = [
        ["Name", "Age", "Address", "Postal Index"],
        ["Ivan Ivanov", 35, "Flat 12, House 5, Lenina Street, Moscow", "101000"],
        ["Anna Petrova", 29, "Flat 45, House 8, Pushkina Street, St. Petersburg", "190000"],
        ["Sergey Sidorov", 42, "Flat 67, House 15, Gagarina Street, Novosibirsk", "630000"],
        ["Olga Smirnova", 31, "Flat 23, House 3, Tverskaya Street, Kazan", "420000"],
        ["Dmitry Fedorov", 27, "Flat 89, House 10, Nevsky Street, Yekaterinburg", "620000"]
    ]
    table = generate_table(data)

    img_path = "opinion.png"
    img = generate_image(img_path)

    file_path = "second_task.tex"
    data_list = [table, img]
    generate_latex_file(file_path, data_list, True)

    output_dir = "output"
    generate_pdf_from_tex(file_path, output_dir)
