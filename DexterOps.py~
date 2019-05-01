#!/usr/bin/python

from Modules.MongoOps import MongoOps
from Modules.ProvisionOps import ProvisionOps


def Start():
    mongo = MongoOps()
    queue = mongo.getQueue()
    #mongo.populate()

    print "Existem %s servicos na fila "%queue.count()

    #for service in mongo.getServiceToRemove():
    #    print "Removendo servico: ",service["_id"]
    #    prov = ProvisionOps(service["_id"])
        #res = prov.RemoveService()
        
    for service in mongo.getServiceToInstall():
        print "Instalando servico: ",service["_id"]
        prov = ProvisionOps(service["_id"])
        res = prov.InstallService()

if __name__ == "__main__":
    Start()
