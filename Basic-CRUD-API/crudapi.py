from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

puppies = []

class PuppyNames(Resource):
    def get(self,name):
        print(puppies)

        # Cycle through list for puppies
        for pup in puppies:
            if pup['name'] == name:
                return pup

        # If you request a puppy not yet in the puppies list
        return {'name':None},404

    def post(self, name):
        # Add  the dictionary to list
        pup = {'name':name}
        puppies.append(pup)
        # Then return it back
        print(puppies)
        return pup

    def delete(self,name):

        # Cycle through list for puppies
        for ind,pup in enumerate(puppies):
            if pup['name'] == name:
                # don't really need to save this
                delted_pup = puppies.pop(ind)
                return {'note':'delete successful'}

        


class AllNames(Resource):

    def get(self):
        # return all the puppies :)
        return {'puppies': puppies}


api.add_resource(PuppyNames, '/puppy/<string:name>')
api.add_resource(AllNames,'/puppies')

if __name__ == '__main__':
    app.run(debug=True)