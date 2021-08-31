from data import DATA

def run():
    all_python_devs = [worker['name'] for worker in DATA if worker['language'] == 'Python']
    all_kodeprint_workers = [worker['name'] for worker in DATA if worker['organization'] == 'KodePrint']
    adults = list(filter(lambda worker: worker['age'] > 18, DATA))
    adults = list(map(lambda worker: worker['name'], adults))
    # Python 3.9 en adelante usa el operador PIPE | <- 
    # old_people = list(map(lambda worker: worker | {"old":worker['age'] > 50}, DATA))
    # Python mayor a 3.5 y menor a 3.9
    old_people = list(map(lambda worker: {**worker, **{"old":worker['age'] > 50}}, DATA))
    

    # CHALLENGE

    all_javascript_devs_2 = list(filter(lambda worker: worker['language'] == 'JavaScript', DATA))
    all_javascript_devs_2 = list(map(lambda worker: worker['name'], all_javascript_devs_2))

    all_kodeprint_workers_2 = list(filter(lambda worker: worker['organization'] == 'KodePrint', DATA))
    all_kodeprint_workers_2 = list(map(lambda worker: worker['name'], all_kodeprint_workers_2))

    adults_2 = [worker['name'] for worker in DATA if worker['age']>18]

    old_people_2 = [{**worker, **{'old': worker['age'] > 50}} for worker in DATA]

    num = 0
    for worker in old_people_2:
        num += 1
        print(num, '-', worker)



if __name__ == '__main__':
    run()