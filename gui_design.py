import customtkinter
import os 


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

        self.button = customtkinter.CTkButton(self, text="Select Text File", command=self.open_file)
        self.button.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=2)
                        
        
        self.name_file_label = customtkinter.CTkLabel(self, text="NameFile", font=('arial', 32 ))
        self.name_file_label.grid(row=1, column=0,  columnspan=2)
        

        self.label_ready = customtkinter.CTkButton(self, text="Convert", font=('arial', 32 ), command=self.convert)
        

    
    def open_file(self):
        self.file_path = customtkinter.filedialog.askopenfilename()
        self.name_file = self.file_path.split('/')[-1]
        if self.name_file.find('.txt') != -1:
            self.name_file_label.configure(text=self.name_file, text_color='black')
            self.label_ready.grid(row=2, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

        else:
             self.name_file_label.configure(
                text='Your Choose Wrong File,\n please check extension of file is txt', 
                text_color= 'red',
                font=('arial', 24)
                )
    def convert(self):
       if self.converter.create_csv_file(self.name_file, self.file_path):
           self.name_file_label.configure(text=f'file Created Done \n Name is: {self.name_file}', text_color='green')
    
    
    def button_callback(self):
        print("button pressed")
        

