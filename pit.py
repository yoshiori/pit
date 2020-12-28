#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, yaml, tempfile
from subprocess import Popen

class Pit:
    VERSION   = "0.5"
    DIRECTORY = os.path.expanduser('~/.pit')
    _config = os.path.join(DIRECTORY, 'pit.yaml')
    _profile = os.path.join(DIRECTORY, 'default.yaml')
    
    @staticmethod
    def set(name, opts={}):
        profile = Pit._load()
        if 'data' in opts:
            result = opts['data']
        else:
            if 'EDITOR' not in os.environ:
                return {}
            
            temp_fd, path = tempfile.mkstemp()
            t = os.fdopen(temp_fd, "w")
            c = yaml.dump(opts['config'] if 'config' in opts else Pit.get(name) ,default_flow_style=False)
            t.write(c)
            t.close()
            Popen([os.environ['EDITOR'],path]).communicate()
            t = open(path)
            result = t.read()
            t.close()
            os.remove(path)

            if result == c:
                print('No Changes')
                if name in profile:
                    return profile[name]
                return

            result = yaml.load(result, Loader=yaml.FullLoader)

        profile[name] = result
        yaml.dump(profile,
                  open(Pit._profile, 'w'),
                  default_flow_style=False)
        return result

    @staticmethod
    def get(name, opts={}):
        load_data = Pit._load()
        ret = load_data[name] if name in load_data else {}
        if 'require' in opts:
            keys = set(opts['require'].keys()) - set(ret.keys())
            if keys:
                for key in keys:
                    ret[key] = opts['require'][key] 
                ret = Pit.set(name,{'config' : ret})
        
        return ret or {'username' : '', 'password' : ''}

    @staticmethod
    def switch(name, opts={}):
        Pit._profile = os.path.join(Pit.DIRECTORY, '%s.yaml' % name)
        config = Pit.config()
        ret = config['profile']
        config['profile'] = name
        yaml.dump(config,
                  open(Pit._config, 'w'),
                  default_flow_style=False)
        return ret

    @staticmethod
    def _load():
        if not os.path.exists(Pit.DIRECTORY):
            os.mkdir(Pit.DIRECTORY)
            os.chmod(Pit.DIRECTORY, 0o700)

        if not os.path.exists(Pit._config):
            yaml.dump({'profile' : 'default'},
                      open(Pit._config, 'w'),
                      default_flow_style=False)
            os.chmod(Pit._config, 0o600)

        Pit.switch(Pit.config()['profile'])

        if not os.path.exists(Pit._profile):
            yaml.dump({}, 
                      open(Pit._profile, 'w'), 
                      default_flow_style=False)
            os.chmod(Pit._profile, 0o600)
        return yaml.load(open(Pit._profile), Loader=yaml.FullLoader) or {}

    @staticmethod
    def config():
        return yaml.load(open(Pit._config), Loader=yaml.FullLoader)

if __name__ == '__main__':
    config = Pit.get('34twitter.com',{'require': {'email':'your email','password':'your password'}})
    print(config)
    print(config['email'])
    print(config['password'])
