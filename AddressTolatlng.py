from flask import Flask, request , jsonify
import simplexml
import requests

app=Flask(__name__)

@app.route('/getAddressDetails', methods=['POST'])
def addressTOlatlng():
    request_data=request.get_json()
    address=request_data['address']
    output_format=request_data['output_format']
    
    
    API_KEY='----------API_KEY------------'
    
    params={
    'key':API_KEY,
    'address':address
    }

    base_url='https://maps.googleapis.com/maps/api/geocode/json?'

    response=requests.get(base_url, params=params)
    response=response.json()

    if response['status']=='OK':
        lat=response['results'][0]['geometry']['location']['lat']
        lng=response['results'][0]['geometry']['location']['lng']
        coordinates={
            "lat":lat,
            "lng":lng
        }
        if output_format=='xml':        
            response=simplexml.dumps(
                {"root":{
                    "address":address,
                    "coordinates":coordinates
                } })
        else:
             response= jsonify(
                Address=address,
                coordinates=coordinates 
            )
    return response
        

if __name__=='__main__':
    app.run()
