import os
from os.path import join, dirname

dotenv_path = join(dirname(__file__), '.env')

if __name__ == '__main__':
    env = os.getenv('ENV')
    print("===> " + env)

