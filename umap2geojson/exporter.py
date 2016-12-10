import json
from urllib.request import urlopen

class Exporter():

    def export(url=None, id=None):
        if id is None:
            if url is not None:
                id = url.rsplit('#',1)[0].split('_')[-1]
            else:
                raise Exception('No url nor map id found')
        response = urlopen("http://umap.openstreetmap.fr/en/map/%d/geojson/"%int(id))
        data = json.loads(response.read().decode('utf8'))
        datalayers = data['properties']['datalayers']
        for layer in datalayers:
            datalayer_id = layer['id']
            response = urlopen("http://umap.openstreetmap.fr/en/datalayer/%d/" % datalayer_id)
            datalayer_json = json.loads(response.read().decode('utf8'))
            return datalayer_json
