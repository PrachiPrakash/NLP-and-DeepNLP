import pandas
import json
import os
class dataset:
    def __init__(self, id):
        self.id = id
        self.dataframe = None
        self.idfield='pn'
    def createdataframe(self,data,orient='index'):
        if data:
            df = pandas.read_json(json.dumps(data), orient=orient)
            self.dataframe = df

    def readdataset(self, data):

        self.data['data'] = data


    def savedataset(self, fname, path='./',orient='index'):
        self.dataframe.to_json(path +'/'+ fname, orient=orient)


    def loaddataset(self,fname,path='./'):
        if os.path.exists(path +'/'+ fname):
            self.createdataframe(json.load(open(path +'/'+ fname)))
            return True
        return False

    def delete(self,fname,path='./'):
        try:
            if os.path.exists(path + '/' + fname):
                os.remove(path + '/' + fname)
                return True
            else:
                return False
        except:
            pass

        return None

    def addrows(self, data):
        if self.data and 'data' in self.data and self.data['data']:

            self.data['data'].update(data)
        else:
            self.data = {"id": self.id, "type": self.type, "fields": self.fields, "data": data}

    def delrows(self, data):
        if self.data and 'data' in self.data and self.data['data']:
            for x in data:
                if x['id'] in self.data['data']:
                    del self.data['data'][x['id']]

    def __init__(self,id):
        self.id=id
        self.dataframe = None
        self.idfield='id'
        self.fields={}
        self.type={}
        self.data=None
    def readdataset(self, data):
        self.fields=data['fields']
        self.type=data['type']
        if 'data' in data and data['data']:
            self.data=data
            self.data['data']=data['data']
    def addrows(self,data):
        if self.data and 'data' in self.data and self.data['data']:

            self.data['data'].update(data)
        else:
            self.data={"id":self.id,"type":self.type,"fields":self.fields,"data":data}
    def delrows(self,data):
        if self.data and 'data' in self.data and self.data['data']:
            for x in data:
                if x['id'] in self.data['data']:
                    del self.data['data'][x['id']]
    def load(self,fname,path='./'):
        if os.path.exists(path+'/'+fname):
            try:
                d=json.load(open(path+'/'+fname))
                self.id=d["id"]
                self.fields=d["fields"]
                self.type=d["type"]
                self.data=d
                return True

            except:
                import traceback

                traceback.print_exc()
                return False
        else:
            return False
