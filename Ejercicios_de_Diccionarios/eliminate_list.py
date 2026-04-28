employee_credentials = {
    'name': 'Cris Ruiz',
    'position': 'Software Engineer',
    'email': 'crisrz@lyfterlearning.com',
    'age': 35,
    'access_level': 'admin'
}
keys_to_remove = ['age', 'access_level']
                    
for key in keys_to_remove: 
    employee_credentials.pop(key)

print (employee_credentials)