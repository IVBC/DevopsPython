#!/usr/bin/python
# -*- coding: UTF-8 -*-
#DevOps.py

from MongoOps import MongoOps
from ProvisionOps import ProvisionOps

def Start():
	mongo = MongoOps()
	queue = mongo.getQueue()

	print "Existem %s servicos na fila "%queue.count()
	
	for service in mongo.getServiceToInstall():
		print "Instalando servico: ",service["_id"]
		prov = ProvisionOps(service["_id"])
		res = prov.InstallService()

if __name__ == "__main__":
    Start()
