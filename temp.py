import tkinter as tk
import ttkbootstrap as tb

class MyComboboxApp:
    def __init__(self, master):
        self.master = master
        master.title("Combobox Value Retrieval")

        # Create a StringVar to hold the combobox value
        self.selected_value = tk.StringVar()

        # Create the Combobox
        self.my_combobox = tb.Combobox(
            master,
            textvariable=self.selected_value,
            values=["Option A", "Option B", "Option C"]
        )
        self.my_combobox.pack(pady=20)

        # Bind the <<ComboboxSelected>> event to a method
        self.my_combobox.bind("<<ComboboxSelected>>", self.on_combobox_select)

        # Label to display the selected value
        self.display_label = tb.Label(master, text="Selected: None")
        self.display_label.pack()

    def on_combobox_select(self, event):
        """
        Callback method executed when a new item is selected in the Combobox.
        """
        current_selection = self.selected_value.get()
        self.display_label.config(text=f"Selected: {current_selection}")

if __name__ == "__main__":
    root = tb.Window(themename="superhero")
    app = MyComboboxApp(root)
    root.mainloop()