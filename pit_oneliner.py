#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, yaml, tempfile
from subprocess import Popen

g = globals()
g.__setitem__("setitem", g.__setitem__)


setitem('VERSION', "0.0.1")
setitem('DIRECTORY', os.path.expanduser('~/.pit'))
setitem('_config', os.path.join(DIRECTORY, 'pit.yaml'))
setitem('_profile', os.path.join(DIRECTORY, 'default.yaml'))
    

def set(name, opts={}):
    setitem('set_profile', _load())
    setitem('set_result', {})
    if opts.has_key('data'):
        setitem('set_result', opts['data'])
    else:
        if not os.environ.has_key('EDITOR'):
            return {}
        setitem('set_if_t', tempfile.NamedTemporaryFile())
        setitem('set_if_c', yaml.dump(opts['config'] if opts.has_key('config') else get(name) ,default_flow_style=False))
        set_if_t.write(c)
        set_if_t.flush()
        setitem('set_if_path', os.path.abspath(t.name))
        Popen([os.environ['EDITOR'],path]).communicate()
        setitem('set_result', open(path).read())
        if set_result == c:
            func_print('No Changes')
            return set_profile[name]
        
        setitem('set_result', yaml.load(result))

    setitem('set_profile_'+ name, set_result)
    yaml.dump(set_profile,
              open(_profile, 'w'),
              default_flow_style=False)
    return set_result

get = lambda name, opts={} :(
    [setitem('load_data', _load())] and \
    [setitem('get_ret', load_data[name] if load_data.has_key(name) else {} )] and \
    [opts.has_key('require') and \
        [setitem('get_for_keys', set(opts['require'].keys()) - set(get_ret.keys()))] and \
        [get_for_keys and \
            [[setitem('get_for_ret_' + key,opts['require'][key])] for key in get_for_keys] and \
            [setitem('get_ret', set(name,{'config' : get_ret}))]]] and \
    (get_ret or {'username' : '', 'password' : ''}) )

switch = lambda name, opts={} :(
    [setitem('_profile', os.path.join(DIRECTORY, '%s.yaml' % name))] and
    [setitem('switch_config', config())] and
    [setitem('switch_ret', switch_config['profile'])] and
    [setitem('switch_config_profie',name)] and
    [yaml.dump(switch_config,
              open(_config, 'w'),
              default_flow_style=False)] and
    switch_ret)

_load = lambda :(
        [[os.mkdir(DIRECTORY)] and [os.chmod(DIRECTORY, 0700)] if not os.path.exists(DIRECTORY) else True]
        and
        [[yaml.dump({'profile' : 'default'}, open(_config, 'w'), default_flow_style=False)] 
         and [os.chmod(_config, 0600)] if not os.path.exists(_config) else True]
        and
        [switch(config()['profile'])]
        and 
        [[yaml.dump({}, 
                    open(_profile, 'w'), 
                    default_flow_style=False)]
         and [os.chmod(_profile, 0600)] if not os.path.exists(_profile) else True]
        
        and (yaml.load(open(_profile)) or {}))

config = lambda : yaml.load(open(_config))

def func_print(data):
    print data;

if __name__ == '__main__':
    setitem('__main__config', get('twitter.com',{'require': {'email':'your email','password':'your password'}}))
    print __main__config
    print __main__config['email']
    print __main__config['password']


