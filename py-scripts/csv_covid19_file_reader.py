import csv

covid_records = list()

class covid_record:
    def __init__(self, direction:str, year:int, date:str, weekday:str, country:str, 
            commodity:str, transport_mode:str, measure:str, value:int, cumulative:int):
        self.direction=direction
        self.year=year
        self.date=date
        self.weekday=weekday
        self.country=country
        self.commodity=commodity
        self.transport_mode=transport_mode
        self.measure=measure
        self.value=value
        self.cumulative=cumulative
    
    def __str__(self) -> str:
        string = "covid_record["+self.direction+", "+self.year+", "+self.date+", "+self.weekday+", "+self.country+", "+self.commodity+", "+self.transport_mode+", "+self.measure+", "+self.value+", "+self.cumulative+"]"
        return string



def run():

    with open('csv-files\effects-of-covid-19-on-trade-at-15-december-2021-provisional.csv', encoding="utf8") as f:

        csv_reader = csv.reader(f)

        i=0
        # добавление данных в массив
        for line in csv_reader:
            # пропустить первую строку и пустые строки
            if i>0 and len(line)!=0:
                covid_records.append(covid_record(*line))
            i+=1
        
        # закрытие коннекшена с файлом
        f.close()