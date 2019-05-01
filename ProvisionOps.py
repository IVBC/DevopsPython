#!/usr/bin/python
# -*- coding: UTF-8 -*-
#ProvisionOps.py

from Service import Service as ServiceClass
from ServiceDao import ServiceDao
from DockerOps import DockerOps

class ProvisionOps:

    _id = ""

    def __init__(self,id):
        self._id = id

    def InstallService(self):
        service = ServiceClass()
        service._id = self._id

        sd = ServiceDao(service)
        service = sd.get()

        print "Sera instalado o Produto ( %s ) para o Client ( %s )"%(service._product._name,service._client._name)
        docker = DockerOps()
        res = docker.createContainer(service._id,service._product._image)

    def RemoveService():
        pass
