my_str = 'абв ыдшва вапабв абв цуекуп ываыуабв'

new_str = ' '.join(list(filter(lambda elem: 'абв' not in elem.lower(), my_str.split())))

print(new_str)