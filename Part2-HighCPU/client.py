import requests, time
import click

UPLOAD_DIR = '/home/tshoot/upload/image.jpg'

@click.command()
@click.option('--uploadimage', is_flag=True, help="upload image to the sever")
@click.option('--uploadencode', is_flag=True, help="upload image to server for encoding")
@click.option('--chaos', is_flag=True, help="Troublemaker endpoint ;)")
def client(uploadimage, uploadencode, chaos):
    code = None
    while True:
        start = time.time()
        if uploadimage:
            files = {'file': open(UPLOAD_DIR,'rb')}
            url = "http://localhost:5000/UploadImage"
            print("Uploading image.jpg to server")
            res = requests.post(url, files=files)
            code = res.status_code
            files['file'].close()
        
        if uploadencode:
            files = {'file': open(UPLOAD_DIR,'rb')}
            url = "http://localhost:5000/UploadAndEncode"
            print("Uploading image.jpg to server for encoding")
            res = requests.post(url, files=files)
            code = res.status_code
            del res # Deleting fetched image to avoid memory leak
            print("Fetched the image from server after encoding")
            files['file'].close()
        
        if chaos:
            url = "http://localhost:5000/chaos"
            requests.get(url)
        
        print(f"StatusCode: {code} Latency: {time.time() - start} seconds")
        #print(res.content)
        time.sleep(1)

if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    client()