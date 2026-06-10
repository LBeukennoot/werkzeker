customers = []

def select_option_input(input_question: str, options: list) -> str:
    print(input_question)
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
            
def text_input(field_name:str, field_type: type):
    print(f'Enter your {field_name}')
    
    while True:
        user_selection = input('> ')
        
        if field_type == int:
            if not user_selection.isdigit():
                print(f"Incorrect input, enter a number.")
                continue
            else:
                return int(user_selection)
        
        if field_type == str:
            return user_selection
        else:
            print('Incorrect input, try again')

def save_data_from_input():
    input_fields = {
        'name': {
            'type': str
        },
        'age': {
            'type': int
        },
        'monthly_expenses': {
            'type': int
        },
        'customer_type': {
            'type': 'string',
            'options': ['new', 'existing', 'premium']
        }
    }
    
    done_adding_customers = False
    
    while not done_adding_customers:
        customer_data = {}
    
        for field_name in input_fields:
            field_data = input_fields[field_name]
            field_name_sanitized = field_name.replace('_', ' ')
            
            if 'options' in field_data:
                input_data = select_option_input(f'Select {field_name} by entering the corresponding number:', field_data['options'])
            else:
                input_data = text_input(field_name_sanitized, field_data['type'])
                
            customer_data[field_name] = input_data
            
        customers.append(customer_data)
            
        add_another_customer = select_option_input('Do you want to add another customer?', ['Yes', 'No'])
        
        if add_another_customer == 'Yes':
            continue
        else:
            return
    
def generate_advice(customer):
    
    advice = "Standaard dienstverlening"
    
    if customer['age'] >= 67:
        advice = 'AOW-check en extra begeleiding'
    
    if customer['monthly_expenses'] > 100:
        advice = 'Check aanvullende regelingen / samenloop'
    
    if customer['customer_type'] == 'premium':
        advice = 'Intensievere begeleiding (complex dossier)'
    
    return advice


# print(
#     generate_advice({
#     'age': 60,
#     'monthly_expenses': 40,
#     'customer_type': 'ba'
# }) 
# )
    
# save_data_from_input()
