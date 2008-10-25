#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, yaml, tempfile
from subprocess import Popen

g = globals()
g.__setitem__("setitem", g.__setitem__)

class Pit:
    VERSION   = "0.0.1"
    DIRECTORY = os.path.expanduser('~/.pit')
    _config = os.path.join(DIRECTORY, 'pit.yaml')
    _profile = os.path.join(DIRECTORY, 'default.yaml')
    
    @staticmethod
    def set(name, opts={}):
        setitem('set_profile', Pit._load())
        setitem('set_result', {})
        if opts.has_key('data'):
            setitem('set_result', opts['data'])
        else:
            if not os.environ.has_key('EDITOR'):
                return {}
            setitem('set_if_t', tempfile.NamedTemporaryFile())
            setitem('set_if_c', yaml.dump(opts['config'] if opts.has_key('config') else Pit.get(name) ,default_flow_style=False))
            set_if_t.write(c)
            set_if_t.flush()
            setitem('set_if_path', os.path.abspath(t.name))
            Popen([os.environ['EDITOR'],path]).communicate()
            setitem('set_result', open(path).read())
            if set_result == c:
                print 'No Changes'
                return set_profile[name]

            setitem('set_result', yaml.load(result))

        setitem('set_profile_'+ name, set_result)
        yaml.dump(set_profile,
                  open(_profile, 'w'),
                  default_flow_style=False)
        return set_result

    @staticmethod
    def get(name, opts={}):
        setitem('load_data', Pit._load())
        setitem('get_ret', load_data[name] if load_data.has_key(name) else {} )
        if opts.has_key('require'):
            setitem('get_for_keys', set(opts['require'].keys()) - set(get_ret.keys()))
            if get_for_keys:
                for key in keys:
                    setitem('get_for_ret_' + key,opts['require'][key]) 
                setitem('get_ret', Pit.set(name,{'config' : get_ret}))
          
        return get_ret or {'username' : '', 'password' : ''}

    @staticmethod
    def switch(name, opts={}):
        setitem('_profile', os.path.join(Pit.DIRECTORY, '%s.yaml' % name))
        setitem('switch_config', Pit.config())
        setitem('switch_ret', switch_config['profile'])
        setitem('switch_config_profie',name)
        yaml.dump(switch_config,
                  open(Pit._config, 'w'),
                  default_flow_style=False)
        return switch_ret

    @staticmethod
    def _load():
        if not os.path.exists(Pit.DIRECTORY):
            os.mkdir(Pit.DIRECTORY)
            os.chmod(Pit.DIRECTORY, 0700)

        if not os.path.exists(Pit._config):
            yaml.dump({'profile' : 'default'},
                      open(Pit._config, 'w'),
                      default_flow_style=False)
            os.chmod(Pit._config, 0600)

        Pit.switch(Pit.config()['profile'])

        if not os.path.exists(Pit._profile):
            yaml.dump({}, 
                      open(Pit._profile, 'w'), 
                      default_flow_style=False)
            os.chmod(Pit._profile, 0600)
        return yaml.load(open(Pit._profile)) or {}

    @staticmethod
    def config():
        return yaml.load(open(Pit._config))

if __name__ == '__main__':
    config = Pit.get('34twitter.com',{'require': {'email':'your email','password':'your password'}})
    print config
    print config['email']
    print config['password']


