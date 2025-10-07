import customtkinter
import os
from CTkMessagebox import CTkMessagebox


class App(customtkinter.CTk):
    def __init__(self, converter, icon_path):
        super().__init__()
        self.converter = converter
        self.title("Convert App")

        if os.path.exists(icon_path):
            self.iconbitmap(icon_path)

        self.geometry("600x500")
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.title_label = customtkinter.CTkLabel(
            self, text="Convert TXT → CSV", font=("Arial", 28, "bold")
        )
        self.title_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.button = customtkinter.CTkButton(
            self, text="Select Text File", command=self.open_file
        )
        self.button.grid(row=0, column=0, padx=20, pady=20,
                         sticky="ew", columnspan=2)

        self.name_file_label = customtkinter.CTkLabel(
            self, text="NameFile", font=("arial", 32)
        )
        self.name_file_label.grid(row=1, column=0, columnspan=2)

        self.label_ready = customtkinter.CTkButton(
            self, text="Convert", font=("arial", 32), command=self.convert_fun
        )

    def open_file(self):

        self.file_path = customtkinter.filedialog.askopenfilename()
        self.name_file = self.file_path.split("/")[-1]

        if self.name_file.find(".txt") != -1:
            self.name_file_label.configure(
                text=self.name_file, text_color="black")
            self.label_ready.grid(
                row=2, column=0, padx=20, pady=20, sticky="ew", columnspan=2
            )

        else:
            self.name_file_label.configure(
                text="Your Choose Wrong File,\n please check extension of file is txt",
                text_color="red",
                font=("arial", 24),
            )

    def convert_fun(self):

        self.path = self.file_path.split("/")[:-1]  # path of file

        # list of all file in path
        self.all_files = os.listdir("\\".join(self.path))

        self.csv_path = os.path.splitext(self.file_path)[0] + ".csv"

        if self.csv_path.split('/')[-1] in self.all_files:
            CTkMessagebox(
                title="Error", message="This File Converted Before", icon="cancel"
            )
        else:

            self.save_as = self.converter.create_csv_file(self.file_path)

            if self.save_as:
                self.name_file_label.configure(
                    text=f"✅ File created successfully!\nSaved as: {os.path.basename(self.save_as)}",
                    text_color="green",
                )

    def button_callback(self):
        print("button pressed")
