def queue_number(list_data):
    if not isinstance(list_data, list):
        return "Your data it is not a list. You can make your data to a list first!"

    if len(list_data) == 0:
        queue_number = "AJU" + "001"
    else:
        recent_queue_number = list_data[-1]['queue_number']
        increment_number = int(recent_queue_number[-3:]) + 1
        queue_number = "AJU" + f"{increment_number:03}"

    return queue_number

def control_number(list_data):
    if not isinstance(list_data, list):
        return "Your data it is not a list. You can make your data to a list first!"

    if len(list_data) == 0:
        control_number = "CTRL" + "001"
    else:
        recent_control_number = list_data[-1]['control_number']
        increment_number = int(recent_control_number[-3:]) + 1
        control_number = "CTRL" + f"{increment_number:03}"

    return control_number

def id(list_data):
    if not isinstance(list_data, list):
        return "Your data it is not a list. You can make your data to a list first!"
    
    if len(list_data) == 0:
        id = 1
    else:
        recent_id = list_data[-1]['id']
        id = int(recent_id) + 1

    return id