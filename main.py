import requests
from PIL import Image
from io import BytesIO
hf_api_key = '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'

def generate_inpainting_image(prompt,image_path,mask_path):
    
    api_url = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-inpainting"
    headers = {'Authorization':f"Bearer{hf_api_key}"}
    with open(image_path,"rb") as img_file:
        image_data = img_file.read()
    with open(mask_path,"rb") as mask_file:
        mask_data = mask_file.read()
    payload = {"inputs":prompt}
    files = {
        "image":("image.png",image_data,'image/png'),
        "mask":("mask.png",mask_data,'image/png')
    }    
    
    response = requests.post(api_url,headers=headers,data = payload,files=files)
    if response.status_code==200:
        inpainted_image = Image.open(BytesIO(response.content))
        return inpainted_image
    else:
        raise Exception(f"Request Failed as status code{response.status_code}")  

def main():
    print('Welcome to the impainting and th Restoration Challenge') 
    print('This activity Allows to restore or transform images')
    print('Provide a bae image,a mask indicating the areas,and a text prompt') 
    print('Type exit to quit')

    while True:
        prompt = input('Enter a description for the impainting or exit to quit') 
        if prompt.lower()=='exit':
            print('Goodbye!')
            break
        image_path = input('Enter the path to the base image') 
        if image_path.lower()=='exit':
            break
        mask_path = input('Enter the path to the mask image') 
        if mask_path.lower()=='exit':
            break
        try:
            print('Inpainting .....')
            res_img = generate_inpainting_image(prompt,image_path,mask_path)
            res_img.show()

            save_opt = input('Do you want to save the inpainted image yes/no').strip().lower()
            if save_opt == 'yes':
                file_name = input('Enter a name to save the inpainted image ').strip()
                res_img.save(f"{file_name}.png\n")
            print("-"*80+'\n')    
        except Exception as e :
            print(f'An error occured :{e}\n')
if __name__ == "__main__":
    main()               