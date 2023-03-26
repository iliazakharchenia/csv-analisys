# импорт функции из другого скрипта, отвечающей за запуск скрипта по созданию коллекции объектов из записей таблицы
from csv_covid19_file_reader import run as covid19_run
# импорт из другого файла коллекции объектов записей из таблицы
from csv_covid19_file_reader import covid_records
from plots_builder import create_plots as plot

# основная функция программы, точка входа в нее
def run() -> None:
    # запуск функции из другого файла
    covid19_run()
    i=1
    for record in covid_records:
        print(str(i)+") "+str(record))
        i+=1
    print("count of covid records = "+str(len(covid_records)))
    plot(covid_records)

if __name__=="__main__":
    run()