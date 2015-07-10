from os import path
import subprocess
THIS_FOLDER = path.dirname(path.abspath(__file__))

def create_session_on_server(host, email):
    print('server_tools.py: create_session_on_server, host: {}, email: {}'.format(host, email))
    session_key = subprocess.check_output(
        [
            'fab',
            'create_session_on_server:email={}'.format(email),
            '--host={}'.format(host),
            '--hide=everything,status',
            ],
        cwd=THIS_FOLDER
        )
    session_key = session_key.decode().strip()
    print('server_tools.py: create_session_on_server, session_key: {}\n'.format(session_key))
    return session_key

def reset_database(host):
    subprocess.check_call(
        ['fab', 'reset_database', '--host={}'.format(host)],
        cwd=THIS_FOLDER
        )
