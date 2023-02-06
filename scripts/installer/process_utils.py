from subprocess import Popen, PIPE
from typing import Tuple, List
import shlex

def run_process_and_log(cmd: List[str], cwd=None, prefix='') -> Tuple[str, str, int]:
    stdout = ''
    stderr = ''
    print(f'Running command: {shlex.join(cmd)}')
    process = Popen(cmd, stdout=PIPE, stderr=PIPE, cwd=cwd, text=True)
    while process.poll() is None:
        if process.stdout is None: continue
        line = process.stdout.readline()
        stdout += line
        if line != '':
            print(f'{prefix}> {line}', end='')

    if process.stderr is not None:
        stderr = process.stderr.read(-1)

    return stdout, stderr, process.returncode
