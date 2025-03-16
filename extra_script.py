import os
Import('env')

env_file_path = os.path.join(env['PROJECT_DIR'], '.env')

if os.path.isfile(env_file_path):
    with open(env_file_path) as f:
        for line in f:
            if line.startswith('#') or not line.strip():
                continue
            
            key, value = line.strip().split('=', 1)
            env.Append(CPPDEFINES=[(key, env.StringifyMacro(value))])

# print('CPPDEFINES: ', env['CPPDEFINES'])
