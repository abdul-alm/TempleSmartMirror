import requests
import json

class Septa(object):
    def traintimes(self,septa_API, parameters, direction, traintime):
        response = requests.get(septa_API, params=parameters)
        trainTimes = response.json()
        for key, value in trainTimes.items():
            key1 = key
        final = (trainTimes[key1][direction])

        for key2, value in final.items():
            key3 = key2
        sort = (json.dumps(final[key3], sort_keys=True, indent=4))
        s = sort.strip('[]')
        trains = s.split('{')
        fullschedule = (trains[traintime])
        return(fullschedule.split('"')[1::2]) # the [1::2] is a slicing which extracts odd values

