import json

# this script below is from a pluralsight AWS training/lab
def lambda_handler(event, context):
    message = 'Hello {} {}! Keep being great!'.format(event['first_name'], event['last_name'])  
    
    # print to CloudWatch logs
    log_message = "LOGS: The message was returned: " + message
    print(message)

    return { 
        'message' : message
    }   
