import csv
import pprint
# matplotlib plotting module
import matplotlib.pyplot as plt
# matplotlib colormap module
import matplotlib.cm as cm
# needed for formatting Y axis
from matplotlib.ticker import FuncFormatter
# Matplotlib font manager
import matplotlib.font_manager as font_manager


"""Include functions for read csv files with WAB report"""
def read_report(file_obj):
    """
    Function for read report from csv file
    :param file_obj: file to read
    :return: table - report in table with rows of the file
    """
    return [row for row in csv.DictReader(file_obj, delimiter=';')]

# bar width
width = .8

if __name__ == '__main__':
    file_name = [r'C:\Users\Dmitry Kononov\Documents\Бастион\Python\Отчеты\Примеры выгрузок\БСпб\statistics\page_connections_log',\
                 r'C:\Users\Dmitry Kononov\Documents\Бастион\Python\Отчеты\Примеры выгрузок\БСпб\statistics\srv-wab-dca-2.bankspb.ru_2018-07-20T17_55_s_connections_per_device.csv',\
                 r'C:\Users\Dmitry Kononov\Documents\Бастион\Python\Отчеты\Примеры выгрузок\БСпб\statistics\srv-wab-dca-2.bankspb.ru_2018-07-20T17_57_s_connections_per_account.csv',\
                 r'C:\Users\Dmitry Kononov\Documents\Бастион\Python\Отчеты\Примеры выгрузок\БСпб\statistics\srv-wab-dca-2.bankspb.ru_2018-07-20T18_02_s_connections_per_user.csv',\
                 r'C:\Users\Dmitry Kononov\Documents\Бастион\Python\Отчеты\Примеры выгрузок\БСпб\statistics\srv-wab-dca-2.bankspb.ru_2018-07-20T18_03_s_connections_duration_per_user.csv',\
                 r'C:\Users\Dmitry Kononov\Documents\Бастион\Python\Отчеты\Примеры выгрузок\БСпб\statistics\srv-wab-dca-2.bankspb.ru_2018-07-20T18_03_s_connections_per_duration.csv',\
                 r'C:\Users\Dmitry Kononov\Documents\Бастион\Python\Отчеты\Примеры выгрузок\БСпб\statistics\srv-wab-dca-2.bankspb.ru_2018-07-20T18_04_s_connections_per_date.csv',\
                 r'C:\Users\Dmitry Kononov\Documents\Бастион\Python\Отчеты\Примеры выгрузок\БСпб\statistics\srv-wab-dca-2.bankspb.ru_2018-07-20T18_04_s_max_simultaneous_connections.csv']
    table = []
    with open(r'/home/dmitrij/Документы/bastion/Отчеты/Примеры выгрузок/БСпб/statistics/page_connections_log.csv', 'r') as infile:
        table = read_report(infile)

    pprint.pprint(table)
    print('Всего записей: ', len(table))
    print(table[0])
