import ttkbootstrap as ttk

class App:
    def __init__(self):
        self.root = ttk.Window()
        
        self.entry = ttk.Entry(self.root, width=30)
        self.entry.pack(pady=10)
        self.entry.bind('<KeyRelease>', self.validate_realtime)
        
        self.status_label = ttk.Label(self.root, text="")
        self.status_label.pack()

    def validate_realtime(self, event):
        text = self.entry.get()
        if text.isalpha() or text == "":
            self.status_label.config(text="✓ Good", bootstyle='success')
        else:
            self.status_label.config(text="Letters only!", bootstyle='danger')

app = App()
app.root.mainloop()