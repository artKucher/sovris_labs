import copy
import json
from random import randint

import psycopg2


class Connection:
    connection = psycopg2.connect(database='lab6', user='postgres', password='postgres', host='localhost', port=5432)
    cursor = connection.cursor()

    def query(self, query_string, params=None):
        self.cursor.execute(query_string, params)
        result = [dict(zip([column[0] for column in self.cursor.description], row)) for row in self.cursor.fetchall()]
        return result

    def insert_into(self, table_name, data):
        for i in data:
            self.cursor.execute(
                "insert into " + table_name + " (id, data) values(%s, %s)",
                (i['id'], json.dumps(i['data']))
            )
            self.connection.commit()


class Utils:
    conn = Connection()

    attributes = conn.query("select distinct json_object_keys(data) from personal_data;")
    number_of_rows = conn.query("select count(*) from personal_data;")[0]['count']
    data = conn.query("select * from personal_data;")
    print(data)

    number_of_attributes_in_u = {}
    rearrangement = {}
    subset_u = {}
    p = {}

    def __init__(self):
        self.create_subsets()
        self.shift_subsets()
        self.data = self.conn.query("select * from personal_data;")
        self.final_matrix()

    # Разбиение на подмножества
    def create_subsets(self):
        for attr in self.attributes:
            self.number_of_attributes_in_u[attr['json_object_keys']] = []
            k = self.number_of_rows
            while k > 0:
                g = randint(2, self.number_of_rows // 3 + 1)
                if k - g == 0 or k - g > 1:
                    self.number_of_attributes_in_u[attr['json_object_keys']].append(g)
                    k -= g
            self.subset_u[attr['json_object_keys']] = len(self.number_of_attributes_in_u[attr['json_object_keys']])

    # Сдвиг в подмножествах
    def shift_subsets(self):
        for attr in self.attributes:
            shift = randint(1, self.subset_u[attr['json_object_keys']] - 1)
            shift_subset = []
            for j in range(self.subset_u[attr['json_object_keys']]):
                shift_subset.append(randint(1, self.number_of_attributes_in_u[attr['json_object_keys']][j] - 1))
            self.p[attr['json_object_keys']] = {}
            self.p[attr['json_object_keys']]['shift'] = shift
            self.p[attr['json_object_keys']]['shift_subset'] = shift_subset

    # Итоговая матрица перестановок
    def final_matrix(self):
        for attr in self.attributes:
            number_of_elements = []
            kk = 0
            for j in range(self.subset_u[attr['json_object_keys']]):
                kt = []
                for o in range(self.number_of_attributes_in_u[attr['json_object_keys']][j]):
                    kt.append(kk)
                    kk += 1
                for k in range(self.p[attr['json_object_keys']]['shift_subset'][j]):
                    kt = kt[-1:] + kt[0:-1]
                number_of_elements.append(kt)
            for k in range(self.p[attr['json_object_keys']]['shift']):
                number_of_elements = number_of_elements[-1:] + number_of_elements[:-1]
            kk = []
            for j in number_of_elements:
                for k in j:
                    kk.append(k)
            self.rearrangement[attr['json_object_keys']] = kk


def depersonalization(data2):
    for i in range(len(Utils.data)):
        for attr in Utils.attributes:
            data2[Utils.rearrangement[attr['json_object_keys']][i]]['data'][attr['json_object_keys']] = Utils.data[i]['data'][attr['json_object_keys']]

    for i in range(len(Utils.data)):
        print(f"{Utils.data[i]} -> {data2[i]}")


def personification(data3):
    for i in range(len(data2)):
        for attr in Utils.attributes:
            data3[i]['data'][attr['json_object_keys']] = data2[Utils.rearrangement[attr['json_object_keys']][i]]['data'][attr['json_object_keys']]

    for i in range(len(data2)):
        print(f"{data2[i]} -> {data3[i]}")


if __name__ == '__main__':
    prepare_data = Utils()
    data2 = copy.deepcopy(prepare_data.data)
    print('depersonalization:')
    depersonalization(data2)

    data3 = copy.deepcopy(data2)
    print('personification:')
    personification(data3)
