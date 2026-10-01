import requests
import handle
import boto3


s3 = boto3.client('s3', region_name='us-west-2')


def request_API(army):
    try:
        name = get_s3_name()
        dump_s3_name()
        
        message = get_s3_message()
        dump_s3_message()
        ##See if the name that is contained in the bucket is Jane, samuel, or john and then flip the necessary card.
        if name.lower() == 'john' or name.lower() == 'jane\'s':
            handle.handle_message('janedoe@gmail.com', '', message, army)
        elif name.lower() == 'john' or name.lower() == 'john\'s':
            handle.handle_message('johndoe@gmail.com', '', message, army)
        elif name.lower() == 'samuel' or name.lower() == 'samuel\'s':
            handle.handle_message('mckaypable@gmail.com', '', message, army)
            
            
        elif any(keyword in name.lower() for keyword in ['samuel Jane', 'samuel\'s Jane\'s', 'samuel and Jane', 'samuel\'s and Jane\'s', 'samuel and Jane\'s']):
            handle.handle_message('mckaypable@gmail.com', '', message, army)
            handle.handle_message('janedoe@gmail.com', '', message, army)
            
        elif any(keyword in name.lower() for keyword in ['Jane samuel', 'Jane\'s samuel\'s', 'Jane and samuel', 'Jane\'s and samuel\'s', 'Jane and samuel\'s']):
            handle.handle_message('mckaypable@gmail.com', '', message, army)
            handle.handle_message('janedoe@gmail.com', '', message, army)
            
            
        elif any(keyword in name.lower() for keyword in ['samuel john', 'samuel\'s john\'s', 'samuel and john', 'samuel\'s and john\'s', 'samuel and john\'s']):
            handle.handle_message('mckaypable@gmail.com', '', message, army)
            handle.handle_message('johndoe@gmail.com', '', message, army)
            
        elif any(keyword in name.lower() for keyword in ['john samuel', 'john\'s samuel\'s', 'john and samuel', 'john\'s and samuel\'s', 'john and samuel\'s']):
            handle.handle_message('mckaypable@gmail.com', '', message, army)
            handle.handle_message('johndoe@gmail.com', '', message, army)
            
        elif any(keyword in name.lower() for keyword in ['Jane john', 'Jane\'s john\'s', 'Jane and john', 'Jane\'s and john\'s', 'Jane and john\'s']):
            handle.handle_message('janedoe@gmail.com', '', message, army)
            handle.handle_message('johndoe@gmail.com', '', message, army)
            
        elif any(keyword in name.lower() for keyword in ['john Jane', 'john\'s Jane\'s', 'john and samuel', 'john\'s and samuel\'s', 'john and samuel\'s']):
            handle.handle_message('janedoe@gmail.com', '', message, army)
            handle.handle_message('johndoe@gmail.com', '', message, army)
        
        elif name.lower() == 'all' or name.lower() == 'all cards':
            handle.handle_message('mckaypable@gmail.com', '', message, army)
            handle.handle_message('johndoe@gmail.com', '', message, army)
            handle.handle_message('janedoe@gmail.com', '', message, army)
            
        else:
            pass
    except: 
        return False
    
    return True


def get_s3_name():
    ## find the bucket and retrieve the name that is contained within it.
    bucket_name = 'frogflipbucket'
    object_key = 'content/name.txt'
    name = s3.get_object(
        Bucket=bucket_name,
        Key=object_key
    )
    
    data = name['Body'].read()
    return data.decode('utf-8')

def dump_s3_name():
    #find the bucket and clear it to prevent an infinite loop of card flipping
    bucket_name = 'frogflipbucket'
    object_key = 'content/name.txt'
    s3.put_object(
        Bucket=bucket_name,
        Key=object_key,
        Body=''
    )

def get_s3_message():
    bucket_name = 'frogflipbucket'
    object_key = 'content/message.txt'
    name = s3.get_object(
        Bucket=bucket_name,
        Key=object_key
    )
    
    data = name['Body'].read()
    return data.decode('utf-8')
    

    
def dump_s3_message():
    bucket_name = 'frogflipbucket'
    object_key = 'content/message.txt'
    s3.put_object(
        Bucket=bucket_name,
        Key=object_key,
        Body=''
    )

if __name__ == "__main__":

     ##just for testing purposes
    get_s3_name()