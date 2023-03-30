import matplotlib.pyplot as plt
import csv_covid19_file_reader as reader
from datetime import datetime
__MINDAY = "01/01/0001"

class point:
    def __init__(self, x:float, y:float) -> None:
        self.x=x
        self.y=y

def day_of_year(date_str: str) -> int:
    date_obj = datetime.strptime(date_str, '%d/%m/%Y')
    return date_obj.timetuple().tm_yday

def days_between(date_str_from: str, date_str_to: str) -> int:
    date_obj_from = datetime.strptime(date_str_from, '%d/%m/%Y')
    date_obj_to = datetime.strptime(date_str_to, '%d/%m/%Y')
    delta_obj = date_obj_to - date_obj_from
    return delta_obj.days

def filter_records_collection(records:list[reader.covid_record], direction:str, country:str, 
            commodity:str, transport_mode:str, measure:str) -> list[reader.covid_record]:
    filtered_records = list()
    for record in records:
        if record.direction.__eq__(direction) and record.country.__eq__(country) and record.commodity.__eq__(commodity) and record.transport_mode.__eq__(transport_mode) and record.measure.__eq__(measure):
            filtered_records.append(record)
    return filtered_records

def get_value_per_day_points_from_records(records:list[reader.covid_record]) -> list[point]:
    points = []
    print("filtered records to plot = "+str(len(records)))
    sorted_records = sorted(list(records), key=lambda r: days_between(__MINDAY, r.date))
    for record in sorted_records:
        points.append(point(days_between(sorted_records[0].date, record.date), record.value))
    print("points to plot = "+str(len(points)))
    return points

def get_cumulative_per_day_points_from_records(records:list[reader.covid_record]) -> list[point]:
    points = []
    print("filtered records to plot = "+str(len(records)))
    sorted_records = sorted(list(records), key=lambda r: days_between(__MINDAY, r.date))
    for record in sorted_records:
        points.append(point(days_between(sorted_records[0].date, record.date), record.cumulative))
    print("points to plot = "+str(len(points)))
    return points

# функция строящая и выводящая в окно график(и)
def create_plots(records:list[reader.covid_record], direction:str, country:str, 
            commodity:str, transport_mode:str, measure:str):
    print("records for analisys = "+str(len(records)))
    
    points = get_cumulative_per_day_points_from_records(filter_records_collection(records=records, direction=direction, 
        country=country, commodity=commodity, transport_mode=transport_mode, measure=measure))
    
    # объявление списков
    # иксы
    arr_x = list()
    # игреки
    arr_fx = list()

    for point in points:
        arr_x.append(point.x)
        arr_fx.append(point.y)

    # построение графика передачей иксов и игреков в метод plt.plot в виде двух списков с одинаковым количеством элементов
    plt.xlabel("days")
    plt.ylabel(direction+" of "+country+", $")
    plt.plot(arr_x, arr_fx)
    plt.show()