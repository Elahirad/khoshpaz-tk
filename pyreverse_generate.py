import os
import subprocess
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='This script generates UML diagram using pyreverse.')

    parser.add_argument('-t', '--test', choices=['yes', 'no'], type=str, required=True,
                        help='include test files or not ? (files starting with test are considered at test files)')

    args = parser.parse_args()

    project_root = 'app'

    py_files = []
    for root, dirs, files in os.walk(project_root):
        for file in files:
            if file.endswith('.py'):
                if args.test == 'yes' or (args.test == 'no' and not file.startswith('test')):
                    py_files.append(os.path.join(root, file))

    command = ['pyreverse', '-o', 'png', '-p', 'SCIPY'] + py_files
    subprocess.run(command)
