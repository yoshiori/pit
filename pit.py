#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, yaml

class Pit:
    Directory = os.path.expanduser('~/.pitPy')
    __config = os.path.join(Directory, 'pit.yaml')
    __profile = os.path.join(Directory, 'default.yaml')

    def set(self, name, opts={}):
        profile = self.__load()
#       t = os.tmpfile()

    def get(self, name, opts={}):
        pass

    def switch(self, name, opts={}):
        self.__profile = os.path.join(self.Directory, '%s.yaml' % name)
        config = self.config()
        ret = config['profile']
        config['profile'] = name
        print config
        yaml.dump(config,
                  open(self.__config, 'w'),
                  default_flow_style=False)
        print 'func switch :' + name
        return ret

    def __load(self):
        if not os.path.exists(self.Directory):
            os.mkdir(self.Directory)
            os.chmod(self.Directory, 0700)

        if not os.path.exists(self.__config):
            yaml.dump({'profile' : 'default'},
                      open(self.__config, 'w'),
                      default_flow_style=False)
            os.chmod(self.__config, 0600)

        self.switch(self.config()['profile'])

        if not os.path.exists(self.__profile):
            yaml.dump({}, 
                      open(self.__profile, 'w'), 
                      default_flow_style=False)
            os.chmod(self.__profile, 0600)

        return yaml.load(open(self.__profile)) or {}

    def config(self):
        return yaml.load(open(self.__config))

if __name__ == '__main__':
    Pit().set('vox.com')
    
'''
switch の opts は何につかうの?


'''
