#
# CSV script for data that came from customers
# Created by: ka <konradadamczykk@gmail.com>
# Date: 2.12.2018.
#

import xlrd
import csv
import django
import os
import argparse
from django.utils import timezone
import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sla.settings")
django.setup()

from sla_app.models import Operator, AggregationType, KeyPerformanceIndicator


def csv_from_excel(file_in, file_out):
    wb = xlrd.open_workbook(file_in)
    sh = wb.sheet_by_name('Sheet1')
    csv_file = open(file_out, 'w')
    wr = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

    for rownum in range(sh.nrows):
        wr.writerow(sh.row_values(rownum))

    csv_file.close()


def get_headers(filename):
    if not os.path.exists(filename):
        return -1

    file_descriptor = open(filename, 'r')
    reader = csv.reader(file_descriptor)

    headers = next(reader, None)

    file_descriptor.close()

    return headers


def is_operator_exists_by_name(operator_name):
    return Operator.objects.filter(name = operator_name).exists()


def create_operator(operator_name):
    operator = ""

    if not is_operator_exists_by_name(operator_name):
        operator = Operator.objects.create(name=operator_name)
        operator.save()
    
    return operator


def get_operator_by_name(operator_name):
    return Operator.objects.get(name = operator_name)


def is_aggr_type_exists_by_name(kpi_type_name):
    return AggregationType.objects.filter(kpi_type = kpi_type_name).exists()


def create_aggregation_type(kpi_type_name):
    aggr_type = ""

    if not is_aggr_type_exists_by_name(kpi_type_name):
        aggr_type = AggregationType.objects.create(kpi_type = kpi_type_name)
        aggr_type.save()
    
    return aggr_type


def get_aggr_type_by_name(kpi_type_name):
    return AggregationType.objects.get(kpi_type = kpi_type_name)


def is_kpi_exists(kpi_name, kpi_operator,
                  kpi_aggr_type, kpi_customer, value):
    return KeyPerformanceIndicator.objects.filter(name = kpi_name,
            operator = kpi_operator,
            aggregation_type = kpi_aggr_type,
            customer = kpi_customer,
            value = value
            ).exists()


def create_kpi(kpi_name, kpi_operator, kpi_aggr_type, kpi_customer, value):
    kpi = ""

    if not is_kpi_exists(kpi_name, kpi_operator, kpi_aggr_type, kpi_customer, value):
        kpi = KeyPerformanceIndicator.objects.create(name=kpi_name,
                value=value, operator=kpi_operator,
                aggregation_type=kpi_aggr_type,
                customer=kpi_customer)
        kpi.save()

    return kpi

# in python3 it does not exist, so implement it purely
def cmp(a, b):
        return (a > b) - (a < b) 


def parse():
    parser = argparse.ArgumentParser(description='Place data from customer B at DB')
    parser.add_argument('filename', type=str, help='filename to parse from customer B')
    parser.add_argument('is_xls', type=int, help='Set if file is .xls')

    args = parser.parse_args()
    path = os.environ.get('SLA_ROOT')
    if not path:
        print("Define SLA_ROOT!!")
        return -1

    path = os.path.join(path, 'sla/static/')
    args.filename = os.path.join(path, args.filename)

    if args.is_xls:
        csv_from_excel(os.path.join(path, args.filename),
                os.path.join(path,'report3_m2m_network_for_customer_b.csv'))


    # Reference headers list, we do not support other types
    headers_list_from_cust_b = ['roaming_partner', 'Month', 'Symbol', 'Customer', 'Country', 'Value', 'Comment', 'KPI Count', 'KPIname', 'Aggr. type']
    headers = get_headers(args.filename)

    if headers == -1:
        print("Couldn't get headers, filename=" + args.filename + "  exiting...")
        return headers


    if cmp(headers_list_from_cust_b, headers):
        print("Given file does not have same headers, aborting...")
        return -1

    file_descriptor = open(args.filename, 'r')
    reader = csv.reader(file_descriptor)

    index = {}
    i = 0;
    for element in headers:
        index[headers[i]] = i
        i = i + 1

    # skip headers
    headers = next(reader, None)

    for row in reader:
        # handle operator
        operator_name = row[index['roaming_partner']]
        if not is_operator_exists_by_name(operator_name):
            o = create_operator(operator_name)
        else:
            o = get_operator_by_name(operator_name)

        # handle aggregation type
        aggr_type_name = row[index['Aggr. type']]
        if not is_aggr_type_exists_by_name(aggr_type_name):
            aggr_t = create_aggregation_type(aggr_type_name)
        else:
            aggr_t = get_aggr_type_by_name(aggr_type_name)

        kpi_name = row[index['KPIname']]
        kpi_value = row[index['Value']]
        kpi_customer = row[index['Customer']]


        # Check for required fields to create KPI
        if (kpi_name and kpi_value and kpi_customer):
            kpi = create_kpi(kpi_name, o, aggr_t, kpi_customer, kpi_value)
            if type(kpi) is str:
                continue;

            # Process other fields
            if row[index['Month']]:
                date_parsed = datetime.datetime.strptime(row[index['Month']], '%m/%d/%Y')
                kpi.created_at = date_parsed

            if row[index['Symbol']]:
                kpi.symbol = row[index['Symbol']]

            if row[index['Country']]:
                kpi.country = row[index['Country']]

            if row[index['Comment']]:
                kpi.comment = row[index['Comment']]

            if row[index['KPI Count']]:
                kpi.kpi_count = int(float(row[index['KPI Count']]))

            kpi.save()

if __name__ == '__main__':
    parse()
