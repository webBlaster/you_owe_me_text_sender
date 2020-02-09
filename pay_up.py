import boto3

def send_sms():
    client = boto3.client('sns','eu-west-1')
    request = client.publish(PhoneNumber='+2348085189108',Message='test')
    print(request)

send_sms()