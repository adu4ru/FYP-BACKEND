import requests
blood_group = { "1": "A+", "2": "A-", "3": "B+", "4": "B-", "5": "AB+", "6": "AB-", "7": "O+", "8": "O-"}

case_list = { "1": "Accident", "2": "Delivery", "3": "Anemia", "4": "Dialysis", "5": "Operation", "6": "Others" }

hospital_list = {"1": "BPKIHS", "2": "Vijaypur Hospital"}

def send_sms(numbers_text, patient_name, blood_group_data, case_data, hospital_data, required_date, number):
    blood = [ ]
    token  = '1955db2f23a27d4e6226a604873c922614f72e6c94547d5035932efe8e9a4989'
    text_message = f'A patient named {patient_name} with the blood group of {blood_group[blood_group_data]} at {hospital_list[hospital_data]} needs blood by {required_date} for {case_list[case_data]}.\nCall at {number} OR \nConfirm your donation through the application.\nYour one step towards it can save a life.'
    r = requests.post(
            "https://sms.aakashsms.com/sms/v3/send/",
            data={ 'auth_token': token,
                    'to'      : numbers_text,
                    'text'    : text_message})
    status_code = r.status_code
    response = r.text
    response_json = r.json()
    return response_json
# print(response_json)