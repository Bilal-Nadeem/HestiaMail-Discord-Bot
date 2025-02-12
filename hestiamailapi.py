import requests

def api(additional_data):
    url = 'api-url-here'
    username = 'username-here'
    domain = 'domain-here'
    data = {
        'hash': 'hash-here',
        'arg1': username,
        'arg2': domain,
    } | additional_data
    response = requests.post(url, data=data)
    return response.text

def add_mail(username, password):
        command = 'v-add-mail-account'
        data = {
            'cmd': command,
            'arg3': username,
            'arg4': password
        }
        return api(data)

def delete_mail(username):
    command = 'v-delete-mail-account'
    data = {
        'cmd': command,
        'arg3': username,
    }
    return api(data)

def change_pass(username, password):
        command = 'v-change-mail-account-password'
        data = {
            'cmd': command,
            'arg3': username,
            'arg4': password
        }
        return api(data)

def list_mail():
    command = 'v-list-mail-accounts'
    data = {
        'cmd': command,
    }
    return api(data)