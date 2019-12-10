import subprocess
import json
from typing import TextIO


def run_code(get_args: dict, post_args: dict, body: str):
    body = json.loads(body)
    program = body['program']
    env = body['env']
    with open('/tmp/program.sipl', "w") as text_file:
        text_file.write(program)
    with open('/tmp/env.file', "w") as text_file:
        text_file.write(env)
    res = subprocess.run([
        'java',
        '-jar',
        '/executable/sipl-interpreter.jar',
        '-e',
        '/tmp/env.file',
        '/tmp/program.sipl'
    ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    stdout = res.stdout.decode('utf8')
    stderr = res.stderr.decode('utf8')
    return json.dumps({
        'ok': not bool(res.returncode),
        'error_code': res.returncode,
        'stdout': stdout,
        'stderr': stderr,
    })


available_get = {}


available_post = {
    'run': run_code
}
