import tkinter as tk
import random

# Funcții pentru generarea poveștilor pentru diferite categorii de vârstă
def poveste_pentru_3_5_ani(nume):
    povesti = [
        f"{nume} este un cățel mic și drăguț care se numește Rex. Rex iubea să se joace în parc cu mingea lui roșie. În fiecare dimineață, Rex îl aștepta nerăbdător pe stăpânul său să vină la parcul din apropiere, unde se jucau împreună timp de ore întregi. Într-o zi, mingea lui Rex a sărit într-o baltă mare, dar el nu s-a speriat deloc. Cu mult curaj, a sărit în apă și și-a adus mingea înapoi la mal. Stăpânul lui Rex a fost atât de mândru de curajul și priceperea cățelului său mic.",
        f"{nume} locuiește într-o pădure îndepărtată, împreună cu o familie de ursuleți. Mama urs și-a învățat puii să găsească miere în stupii de albine. Împreună, familia de ursuleți mergea în fiecare zi în căutare de miere delicioasă. Cu răbdare și pricepere, mama urs îi învăța pe puii săi cum să se apropie de stupuri fără să provoace albinele. În cele din urmă, puii de urs au devenit niște culegători de miere pricepuți, iar familia lor a trăit fericită pentru totdeauna."
    ]
    return random.choice(povesti), "blue"  # Se întoarce o poveste și culoarea textului

def poveste_pentru_6_8_ani(nume):
    povesti = [
        f"{nume} este un cavaler curajos care își luase armura și plecase să salveze prințesa de la dragonul fioros. Cavalerul a călătorit prin păduri întunecate, a traversat râuri adânci și a învins monștri înfricoșători pentru a ajunge la castelul în care era ținută prizonieră prințesa. Cu inima plină de curaj și spada în mână, cavalerul a înfruntat dragonul și l-a învins, eliberând prințesa și aducând pacea în regat.",
        f"Alice și prietenii săi, printre care se numără și {nume}, au pornit într-o călătorie fantastică în țara minunilor, unde au întâlnit creaturi magice și au trăit aventuri nebănuite. Călătoria lor i-a dus prin păduri fermecate, pe lângă râuri pline de zâne și în vârfuri de munte înzăpezite. Cu fiecare pas pe care-l făceau, ei descopereau noi minuni și învățau lecții importante despre prietenie, curaj și încredere în sine."
    ]
    return random.choice(povesti), "green"  # Se întoarce o poveste și culoarea textului

def poveste_pentru_9_12_ani(nume):
    povesti = [
        f"{nume} trăiește într-o lume futuristă, unde se alătură unui grup de tineri genii pentru a opri o conspirație care amenință să distrugă lumea. Acești tineri eroi, printre care se numără și {nume}, sunt înzestrați cu abilități extraordinare și sunt conduși de un lider carismatic. Cu inovație și curaj, ei dezvăluie planurile malefice ale conspiratorilor și îi înfruntă pentru a-și proteja lumea.",
        f"{nume} descoperă că are puteri magice și se alătură unei școli secrete pentru a învăța să-și controleze abilitățile și să lupte împotriva forțelor întunecate. La școală, el face noi prieteni și învață lecții importante despre prietenie, loialitate și sacrificiu. Împreună, ei se pregătesc să înfrunte forțele întunecate care amenință să cucerească lumea lor magică."
    ]
    return random.choice(povesti), "red"  # Se întoarce o poveste și culoarea textului

# Funcție pentru selectarea povestii în funcție de vârstă și nume
def selecteaza_poveste(varsta, nume):
    if varsta < 3:
        return "Poveștile sunt potrivite pentru copii de la 3 ani în sus.", "black"  # Poveste generică pentru vârsta mică
    elif varsta <= 5:
        return poveste_pentru_3_5_ani(nume)  # Alege o poveste pentru vârsta specifică
    elif varsta <= 8:
        return poveste_pentru_6_8_ani(nume)  # Alege o poveste pentru vârsta specifică
    elif varsta <= 12:
        return poveste_pentru_9_12_ani(nume)  # Alege o poveste pentru vârsta specifică
    else:
        return "Din păcate, nu avem povești potrivite pentru această vârstă.", "black"  # Poveste generică pentru vârsta mare

# Funcție pentru afișarea poveștii în fereastra de text
def afiseaza_poveste():
    nume = nume_entry.get()
    varsta = int(varsta_entry.get())
    text_poveste.delete(1.0, tk.END)  # Șterge orice text existent în fereastra de text
    text, culoare = selecteaza_poveste(varsta, nume)  # Selectează povestea și culoarea textului
    text_poveste.insert(tk.END, text, "normal")  # Adaugă povestea în fereastra de text
    text_poveste.config(fg=culoare)  # Setează culoarea textului

if __name__ == "__main__":
    # Creare și configurare fereastra principală
    root = tk.Tk()
    root.title("Biblioteca de Povești")

    # Creare etichetă și câmp pentru introducerea numelui copilului
    nume_label = tk.Label(root, text="Introdu numele copilului:")
    nume_label.pack()
    nume_entry = tk.Entry(root)
    nume_entry.pack()

    # Creare etichetă și câmp pentru introducerea vârstei copilului
    varsta_label = tk.Label(root, text="Introdu vârsta copilului:")
    varsta_label.pack()
    varsta_entry = tk.Entry(root)
    varsta_entry.pack()

    # Creare fereastră de text pentru afișarea poveștii
    text_poveste = tk.Text(root, wrap=tk.WORD, height=10, width=50)
    text_poveste.tag_configure("normal", font=("Arial", 10))  # Configurare stil de text normal
    text_poveste.pack()

    # Creare buton pentru afișarea poveștii
    afiseaza_buton = tk.Button(root, text="Afișează Poveste", command=afiseaza_poveste)
    afiseaza_buton.pack()

    # Rularea buclei principale a aplicației
    root.mainloop()