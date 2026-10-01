import requests
import handle
import boto3


s3 = boto3.client('s3', region_name='us-west-2')


def request_API(army):
    try:
        name = get_s3_name()
        print(name)
        dump_s3_name()
        
        message = get_s3_message()
        dump_s3_message()
        ##See if the name that is contained in the bucket is jenny, sam, or paul and then flip the necessary card.
        if name.lower() == 'john' or name.lower() == 'jane\'s':
            handle.handle_message('janedoe@gmail.com', '', message, army)
        elif name.lower() == 'john' or name.lower() == 'john\'s':
            handle.handle_message('johndoe@gmail.com', '', message, army)
        elif name.lower() == 'sam' or name.lower() == 'sam\'s':
            handle.handle_message('mckaypable@gmail.com', '', message, army)
            
            
        elif any(keyword in name.lower() for keyword in ['sam jenny', 'sam\'s jenny\'s', 'sam and jenny', 'sam\'s and jenny\'s', 'sam and jenny\'s']):
            handle.handle_message('mckaypable@gmail.com', '', message, army)
            handle.handle_message('janedoe@gmail.com', '', message, army)
            
        elif any(keyword in name.lower() for keyword in ['jenny sam', 'jenny\'s sam\'s', 'jenny and sam', 'jenny\'s and sam\'s', 'jenny and sam\'s']):
            handle.handle_message('mckaypable@gmail.com', '', message, army)
            handle.handle_message('janedoe@gmail.com', '', message, army)
            
            
        elif any(keyword in name.lower() for keyword in ['sam paul', 'sam\'s paul\'s', 'sam and paul', 'sam\'s and paul\'s', 'sam and paul\'s']):
            handle.handle_message('mckaypable@gmail.com', '', message, army)
            handle.handle_message('johndoe@gmail.com', '', message, army)
            
        elif any(keyword in name.lower() for keyword in ['paul sam', 'paul\'s sam\'s', 'paul and sam', 'paul\'s and sam\'s', 'paul and sam\'s']):
            handle.handle_message('mckaypable@gmail.com', '', message, army)
            handle.handle_message('johndoe@gmail.com', '', message, army)
            
        elif any(keyword in name.lower() for keyword in ['jenny paul', 'jenny\'s paul\'s', 'jenny and paul', 'jenny\'s and paul\'s', 'jenny and paul\'s']):
            handle.handle_message('janedoe@gmail.com', '', message, army)
            handle.handle_message('johndoe@gmail.com', '', message, army)
            
        elif any(keyword in name.lower() for keyword in ['paul jenny', 'paul\'s jenny\'s', 'paul and sam', 'paul\'s and sam\'s', 'paul and sam\'s']):
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