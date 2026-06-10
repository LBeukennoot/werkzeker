customers = []

def select_option_input(input_question: str, options: list) -> str:
    """
    Function that lets the user choose one of the defined options.
    Using the while loop, it constantly loops over the same code
    untill the user enters a valid option, what exits the loop with
    'return'. The function is reused in the creation of customers,
    but also to check if another customer is going to be added.
    The user can only enter a number (text is not allowed) and a 
    number that actually is an option. Any given inputis handled 
    and a suited 'error' is given to the user.
    """
    
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
    """
    Allows the user to enter either a string or integer as input.
    The function props define which variable type is allowed, and
    gives a suitable 'error' when an incorrect value has been entered.
    """
    
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
    """
    Combines the two input functions and asks the user for input
    using the input() functionality. The field options are defined
    at input_fields, including field types (and options). The
    function also handles whether the user wants to insert another
    customer, and is saved globally so other functions can use
    the data.
    """
    
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
    
    while True:
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
    """
    Generates advice based on the user input. Prioritized data
    gets returned first and ignores the other options.
    """
    
    if customer['customer_type'] == 'premium':
        return 'Intensievere begeleiding (complex dossier)'
        
    if customer['monthly_expenses'] > 100:
        return 'Check aanvullende regelingen / samenloop'
    
    if customer['age'] >= 67:
        return 'AOW-check en extra begeleiding'
    
    return "Standaard dienstverlening"


def print_summary():
    """
    Combines all functionalities and prints a summary of all
    submitted customers.
    """
    
    save_data_from_input()
    
    i = 0
    
    while i < len(customers):
        advice = generate_advice(customers[i])
        print(f'{customers[i]['name']}:\n{advice}\n')
        i +=1

print_summary()