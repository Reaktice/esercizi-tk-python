import tkinter as tk

# Funzione per stampare un'etichetta senza input
def stampa_etichetta():
    text = "Etichetta di prova da funzione"
    text_output = tk.Label(window, text=text, fg="#FF0000", font=("Helvetica", 16))
    text_output.grid(row=1, column=1, sticky="W")

# Funzione per stampare un'etichetta con input
def stampa_etichetta_input():

    # Convertire gli input in numeri 
    numero1 = int(input_text.get()) 
    numero2 = int(input_text2.get()) 
    somma = numero1 +numero2
    testo = somma
    text_output1 = tk.Label(window, text=testo, fg="#FF0000", font=("Helvetica", 16))
    text_output1.grid(row=3, column=1, sticky="W")

# Creazione della finestra principale
window = tk.Tk()
window.title("Finestra di prova")
window.geometry("600x600")
window.resizable(False, False)
window.configure(background="gray")

# Creazione della prima etichetta
etichetta = tk.Label(window, text="Etichetta di prova", fg="#FF0000", font=("Helvetica", 16))
etichetta.grid(row=0, column=0, sticky="W", padx=10, pady=10)

# Creazione del primo bottone
first_button = tk.Button(window, text="Clicca!", command=stampa_etichetta)
first_button.grid(row=1, column=0, sticky="W")

# Creazione del campo di input
input_text = tk.Entry(window)
input_text.grid(row=2, column=0, sticky="W")

input_text2 = tk.Entry(window)
input_text2.grid(row=2, column=1, sticky="W")

# Creazione del secondo bottone
second_button = tk.Button(window, text="Clicca!", command=stampa_etichetta_input)
second_button.grid(row=3, column=0, sticky="W")

# Avvio del ciclo principale della finestra
if __name__ == "__main__":
    window.mainloop()
