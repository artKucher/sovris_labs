if __name__ == '__main__':
    actives = input('Введите названия активов через символ %: ').split('%')
    actives_value = {active: {} for active in actives}
    # Заполняем таблицу активов
    for active in actives:
        for consequence in ['К', 'Ц', 'Д']:
            current = {}
            print(f'Актив: {active}. Последствие: {consequence}.')
            current['Тип ущерба'] = input(f'Введите тип ущерба: ')
            current['Ущерб'] = int(input(f'Введите ущерб (примерное количество в рублях): '))
            current['Примечание'] = input(f'Введите примечание: ')
            actives_value[active][consequence] = current

    # Выводим таблицу
    print(f"{'Актив':<15} {'Последствие угрозы':<20} {'Тип ущерба':<15} {'Ущерб':<10} {'Примечание':<15}")
    for k, v in actives_value.items():
        for type, consequence in v.items():
            print(f"{k:<15} {type:<20} {consequence['Тип ущерба']:<15} {consequence['Ущерб']:<10} {consequence['Примечание']:<15}")

    # Заполняем угрозы
    for active in actives:
        for consequence in ['К', 'Ц', 'Д']:
            current = {}
            print(f'Актив: {active}. Последствие: {consequence}.')
            threats = input('Введите угрозы через символ %: ').split('%')
            for threat in threats:
                print(f'Угроза: {threat}.')
                threat_dict = {
                    'Частота': float(input(f'Введите частоту в год: ')),
                    'Вероятность': float(input(f'Введите вероятность реализации: ')),
                    'Стоимость защиты': int(input(f'Введите стоимость защиты: '))
                }
                current[threat] = threat_dict
            actives_value[active][consequence]['Угрозы'] = current

    # Вычисляем ALE и ROI
    for active_name, active in actives_value.items():
        for consequence_name, consequence in active.items():
            for threat_name, threat in consequence['Угрозы'].items():
                print(f'Актив: {active_name}. Последствие: {consequence_name}. Угроза: {threat_name}.')
                ALE = consequence["Ущерб"] * threat["Частота"] * threat["Вероятность"]
                print(f'ALE: {ALE}')
                print(f'ROI: {(ALE - threat["Стоимость защиты"]) / threat["Стоимость защиты"]}')
