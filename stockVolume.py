import originpro as op
import os
import requests
from tkinter import *

#Stock Name to watch
STOCK_NAME = ""
#AlphaVantage API endpoint
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
#AlphaVantage API key (Tragen Sie hier Ihren AplhaVantage API key ein.)
STOCK_API_KEY = "XXX"

#Heute als julianisches Datum
today = op.utils.lt_int("today()")
dateList = []


#TK Interface
def button_clicked():
    #Wert aus Textbox holen
    STOCK_NAME = my_input.get()

    #AlphaVantage Parameter
    stock_params = {
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol": STOCK_NAME,
        "apikey": STOCK_API_KEY,
    }
    try:
        #API Abfrage
        stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)
        stock_response.raise_for_status()
        stock_data = stock_response.json()["Time Series (Daily)"]
        stock_list = [value for (key, value) in stock_data.items()]

        #Arbeitsblatt vorbereiten
        wks = op.new_sheet()
        wks.cols = 8
        wks.as_date(0,'dd-MMM-yy')

        #Liste mit Daten füllen
        for i in range(0, 100):
            dateList.append(today - i)

        #Arbeitsblatt füllen und Sortierung invertieren
        wks.from_list(0, dateList, 'Zeit')
        for i in range(0, len(stock_list)):
            wks.from_dict(stock_list[i],1,i)
        wks.set_label(6, 'Volumen',)
        wks.sort(0)

        #Erstelle das Liniendiagramm
        graph = op.new_graph(template='line')
        gl=graph[0]
        plot = gl.add_plot(f'{wks.lt_range()}!(?,7)')
        gl.rescale()

        #Fenster schliessen
        window.destroy()

    except:
        my_label.config(text="Geben Sie einen gültigen Aktiennamen ein: ")


#Fenster erstellen
window = Tk()
window.title("Stock Watch Demo")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)

#Label
my_label = Label(text="Geben Sie einen Aktiennamen ein: ", font=("Arial", 14, "bold"))
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

#Button
my_button = Button(text="Los", command=button_clicked)
my_button.grid(column=0, row=2)

#Entry
my_input = Entry(width=10)
my_input.grid(column=0, row=1)

#Main Loop
window.mainloop()
