## for this version, i ll be using an LLM to perform the existence for me, later i ll have to finetune a yolo model and train it using custom imagesimport os
import os
from google import genai
from dotenv import load_dotenv
from huggingface_hub import InferenceClient


load_dotenv()


def check_ai(img):
    api_key = os.getenv("Hug_Face")
    if not api_key:
        raise ValueError("Missing Hug_Face API key")

    client = InferenceClient(
        provider="hf-inference",
        api_key=api_key,
    )

    output = client.image_classification(img, model="umm-maybe/AI-image-detector")
    human_score=0
    ai_score=0
    for result in output:
        if(result.label=="human"):
            human_score=round(result.score,2)
        else:
            ai_score=round(result.score,2)

    return [human_score,ai_score]

def check_output(list):
    h_score=list[0]
    ai_score=list[1]
    if(ai_score>=0.65):
        return True
    return False
    
def check_auth(img,category):
    api_key=os.getenv("Gemini")
    if not api_key:
        raise ValueError("missing gemini api key")
    client=genai.Client(api_key=api_key)
    my_file=client.files.upload(file=img)    
    
    prompt=f"""consider yourself highly proficient in finding things in images. 
    You dont have to analyse the image and nor do you have to run it against the input text. You have to form a confidence score using the following means:-
    a)match whether the keyword mentioned in the text exists in the image or not.for example:if the text is traffic lights failure, the keyword here is traffic light.search for it
    Give this a 75 percentage weightage

    b)check whether the action mentioned in the text is actually present in the image or not. for example if the text mentions a traffic light failure, try and figure out whether it is working or not.\
    Give this a 25 percetage weightage 
    .You must output a confidence score using a scale of 0.0-1.0, round the confidence score upto 2 decimal places.
    The object to look for is: {category}
    output only and only the confidence score nothing more nothing less."""
    
    output_gemini=client.interactions.create(model='gemini-3.5-flash',input=[{"type":"text","text":prompt},
                                                                            {
                                                                                "type":"image",
                                                                                "uri":my_file.uri,
                                                                                "mime_type":my_file.mime_type  
                                                                            } ])
    return float(output_gemini.output_text)






if __name__ == "__main__":
    output=check_ai("/mnt/c/Users/2.LAPTOP-GMFP48KM/OneDrive/Pictures/Screenshots 1/Screenshot 2026-04-16 115127.png")
    flag=check_output(output)
    conf_score=check_auth("/mnt/c/Users/2.LAPTOP-GMFP48KM/OneDrive/Desktop/images.jpg","traffic light failure")
    print(conf_score)
    
    
    
