customer_data = []

def select_option_input(field_name: str, options: list) -> str:
    print(f'Select {field_name}:')
    for i in range(1, len(options) + 1):
        print(f'[{i}] {options[i-1]}')
    
    
    while True:
        user_selection = input('> ')
        
        if not user_selection.isdigit():
            print("Incorrect input, enter a number.")
            continue
        
        user_selection_number = int(user_selection)
        
        if 1 <= user_selection_number <= len(options):
            return options[user_selection_number - 1]
        else:
            print(f"Incorrect input, enter a number between 1 and {len(options)}.")

def save_data_from_input():
    input_fields = {
        # 'name': {
        #     'type': 'string'
        # },
        # 'age': {
        #     'type': 'int'
        # },
        # 'expenses': {
        #     'type': 'int'
        # },
        'customer_type': {
            'type': 'string',
            'options': ['new', 'existing', 'premium']
        }
    }
    
    for field_name in input_fields:
        field_data = input_fields[field_name]
        if 'options' in field_data:
            select_option_input(field_name, field_data['options'])
        else:
            input(f"Enter your {field_name.replace('_', ' ')} \n> ")
        
save_data_from_input()
# print(customer_data)