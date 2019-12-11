import subprocess
import json

def run_code(get_args: dict, post_args: dict, body: str):
    body = json.loads(body)
    program = body['program']
    env = body['env']
    with open('/tmp/program.sipl', "w") as text_file:
        text_file.write(program)
    with open('/tmp/env.file', "w") as text_file:
        text_file.write(env)
    try:
        res = subprocess.run([
            'java',
            '-jar',
            '/executable/sipl-interpreter.jar',
            '-e',
            '/tmp/env.file',
            '/tmp/program.sipl'
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=2)
        retcode = res.returncode
        stdout = res.stdout.decode('utf8')
        stderr = res.stderr.decode('utf8')
    except subprocess.TimeoutExpired:
        retcode = -1
        stdout = None
        stderr = 'Timeout after 2 seconds!'

    return json.dumps({
        'ok': not bool(retcode),
        'error_code': retcode,
        'stdout': stdout,
        'stderr': stderr,
    })


available_get = {}


available_post = {
    'run': run_code
}
