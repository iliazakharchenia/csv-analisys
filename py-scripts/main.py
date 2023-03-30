# импорт функции из другого скрипта, отвечающей за запуск скрипта по созданию коллекции объектов из записей таблицы
from csv_covid19_file_reader import run as covid_reader_run
# импорт из другого файла коллекции объектов записей из таблицы
from csv_covid19_file_reader import covid_records
from plots_builder import create_plots as plot_1

# основная функция программы, точка входа в нее
def run() -> None:
    covid_reader_run()
    plot_1(covid_records, direction="Exports", country="All", commodity="All", transport_mode="All", measure="$")

if __name__=="__main__":
    run()