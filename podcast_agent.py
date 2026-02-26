
# %% [Setup and Imports]
import time
from io import BytesIO
from PIL import Image
from IPython.display import display
from google import genai
from google.genai import types

# 1. Configuration - Replace with your key
API_KEY = ""
MODEL_ID = "gemini-2.5-flash"  # Using the active model from your list

client = genai.Client(api_key=API_KEY)

# %% [Core Functions]

def generate_visual(image_prompt):
    """
    Generates an image using Gemini's multimodal output capabilities
    and displays it directly in the VS Code Interactive Window.
    """
    print(f"\n🎨 [AI Artist is drawing: {image_prompt}...]")
    try:
        # Requesting a single image from the model
        response = client.models.generate_content(
            model=MODEL_ID,
            contents=[f"Create a vibrant, kid-friendly historical illustration: {image_prompt}"],
            config=types.GenerateContentConfig(
                response_mime_types=['image/jpeg']
            )
        )
        
        # Check if we got image data back
        if response.candidates[0].content.parts[0].inline_data:
            img_data = response.candidates[0].content.parts[0].inline_data.data
            img = Image.open(BytesIO(img_data))
            display(img)  # This renders the image in VS Code
            print("✅ Visual ready!\n")
        else:
            print("❌ No image data returned.")
            
    except Exception as e:
        print(f"⚠️ Image generation error: {e}")

def run_podcast_session(user_topic):
    """
    Streams the podcast script and triggers image generation
    whenever the agent decides a visual is needed.
    """
    system_prompt = """
    You are 'Professor Pharaoh,' an enthusiastic and funny host of a kids' history podcast.
    Your tone is adventurous and educational.
    
    STRICT RULE: When you want to show a picture to the kids, you MUST use the following 
    exact tag in your text: [IMAGE: description of the image]. 
    Example: 'The Nile was huge! [IMAGE: A wide shot of the blue Nile river with a boat]'
    """

    print(f"🎙️ [Recording Episode: {user_topic}]\n" + "="*50)

    # Start the text stream
    stream = client.models.generate_content_stream(
        model=MODEL_ID,
        contents=[
            {"role": "user", "parts": [{"text": system_prompt}]},
            {"role": "user", "parts": [{"text": f"Start a podcast episode about: {user_topic}"}]}
        ]
    )

    for chunk in stream:
        for part in chunk.candidates[0].content.parts:
            text = part.text
            
            # Check for the Image Tag [IMAGE: ...]
            if "[IMAGE:" in text:
                # Split text to handle parts before and after the tag
                pre_text, post_tag = text.split("[IMAGE:", 1)
                print(pre_text, end="", flush=True)
                
                # Extract the description inside the brackets
                if "]" in post_tag:
                    image_desc, remaining_text = post_tag.split("]", 1)
                    generate_visual(image_desc.strip())
                    print(remaining_text, end="", flush=True)
                else:
                    # If tag is split across chunks, this handles it gracefully
                    print("... (rendering visual) ...", end="")
            else:
                print(text, end="", flush=True)
                
        time.sleep(0.05) # Adds a natural 'reading' delay

# %% [Run the Agent]
# Change this topic to explore different parts of Egypt!
run_podcast_session("The secret chambers of the Great Pyramid of Giza")
