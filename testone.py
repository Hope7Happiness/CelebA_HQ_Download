import hashlib

def checksum(filename, method='sha1'):
    data = open(filename, 'rb').read()
    if method == 'sha1':
        return hashlib.sha1(data).hexdigest()
    elif method == 'md5':
        return hashlib.md5(data).hexdigest()
    else:
        raise ValueError('Invalid method: %s' % method)
    return None

print(checksum('./celebA/Anno/list_landmarks_celeba.txt'))
print(checksum('./celebA-HQ/deltas07000.zip'))
print(checksum('./celebA-HQ/image_list.txt'))