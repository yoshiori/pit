#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, yaml, tempfile
from subprocess import Popen

class Pit:
    VERSION   = "0.0.1"
    DIRECTORY = os.path.expanduser('~/.pit')
    __config = os.path.join(DIRECTORY, 'pit.yaml')
    __profile = os.path.join(DIRECTORY, 'default.yaml')
    
    @staticmethod
    def set(name, opts={}):
        profile = Pit.__load()
        ret = {}
        if opts.has_key('data'):
            ret = opts['data']
        else:
            if not os.environ.has_key('EDITOR'):
                return {}
            t = tempfile.NamedTemporaryFile()
            c = yaml.dump(opts['config'] if opts.has_key('config') else Pit.get(name) ,default_flow_style=False)
            t.write(c)
            t.flush()
            path = os.path.abspath(t.name)
            Popen([os.environ['EDITOR'],path]).communicate()
            result = open(path).read()
            if result == c:
                print 'No Changes'
            result = yaml.load(result)
            profile[name] = result
            yaml.dump(profile,
                      open(Pit.__profile, 'w'),
                      default_flow_style=False)
            return result

    @staticmethod
    def get(name, opts={}):
        load_data = Pit.__load()
        ret = load_data[name] if load_data.has_key(name) else {} 
        if opts.has_key('require'):
            for k, v in opts['require'].iteritems():
                ret[k] = v
            ret = Pit.set(name,{'config' : ret})
        return ret or {'username' : '', 'password' : ''}

    @staticmethod
    def switch(name, opts={}):
        Pit.__profile = os.path.join(Pit.DIRECTORY, '%s.yaml' % name)
        config = Pit.config()
        ret = config['profile']
        config['profile'] = name
        yaml.dump(config,
                  open(Pit.__config, 'w'),
                  default_flow_style=False)
        return ret

    @staticmethod
    def __load():
        if not os.path.exists(Pit.DIRECTORY):
            os.mkdir(Pit.DIRECTORY)
            os.chmod(Pit.DIRECTORY, 0700)

        if not os.path.exists(Pit.__config):
            yaml.dump({'profile' : 'default'},
                      open(Pit.__config, 'w'),
                      default_flow_style=False)
            os.chmod(Pit.__config, 0600)

        Pit.switch(Pit.config()['profile'])

        if not os.path.exists(Pit.__profile):
            yaml.dump({}, 
                      open(Pit.__profile, 'w'), 
                      default_flow_style=False)
            os.chmod(Pit.__profile, 0600)
        return yaml.load(open(Pit.__profile)) or {}

    @staticmethod
    def config():
        return yaml.load(open(Pit.__config))

if __name__ == '__main__':
    config = Pit.get('twitter.com',{'require': {'email':'your email','password':'your password'}})
    print config['email']
    print config['password']
