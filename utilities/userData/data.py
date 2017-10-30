import json

class Data(object):
    def storeData(self, name, weight):
        data = {'People': [{'name': name, 'weight':[weight]}]}
        try:
            with open('data.json') as outfile_r:
                try:
                    source_data = json.load(outfile_r)
                    new_name = True
                    for ppl in source_data['People']:
                        if ppl['name']==ID:
                            ppl['weight'].append(weight)
                            new_name = False
                    if new_name:
                        source_data['People'].append({'name': ID, 'weight':[weight]})
                    storage = source_data
                except:
                    storage = data
            with open('data.json','w') as outfile_w:
                json.dump(storage, outfile_w, sort_keys=True, indent=4)
        except:
            with open('data.json','w') as outfile_w:
                storage = data
                json.dump(storage, outfile_w, sort_keys=True, indent=4)

    def readData(self, name):
        with open('data.json') as json_file:
            try:
                source_data = json.load(json_file)
                for person in source_data['People']:
                    if person['name']==name:
                        return json.dumps(person['weight'], indent=4)
            except:
                print('Error')
