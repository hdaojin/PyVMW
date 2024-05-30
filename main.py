import json
import httpx
import asyncio

# Define the URL to the API
url = "http://127.0.0.1:8697/api"

# Define the authorization
headers = {
    # "Accept": "application/vnd.vmware.vmw.rest-v1+json",
    "Content-Type": "application/vnd.vmware.vmw.rest-v1+json",
    "Authorization": "Basic dm13YXBpOlNraWxsczM5IQ=="
}


# Get VMs list
async def get_vms():
    endpoint = "/vms"
    async with httpx.AsyncClient() as client:
        response = await client.get(url + endpoint, headers=headers)
        return response.json()
    
# Start VM
async def start_vm(vm_id):
    endpoint = f"/vms/{vm_id}/power"
    data = "on"
    async with httpx.AsyncClient() as client:
        response = await client.put(url + endpoint, headers=headers, data=data)
        return response.json()

# main function
if __name__ == "__main__":
    #Get the VMs list
    vms = asyncio.run(get_vms())
    print(json.dumps(vms, indent=4)) 

    # Start the first VM
    # vm_id = "R6CD18IAMP0FRT5UICAJHRPSNO1FVLFI"
    # response = asyncio.run(start_vm(vm_id))
    # print(json.dumps(response, indent=4))

    