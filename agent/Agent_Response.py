from dotenv import load_dotenv
from google import genai
import os
import json
load_dotenv()

def user_response(complaint,cat,dept):
    api_key=os.getenv("Gemini")
    if not api_key:
        raise ValueError("Key not found")
    client= genai.Client(api_key=api_key)

    
    prompt = f"""
You are assisting citizens who have submitted public grievances.

Your task is to generate exactly TWO practical instructions that the citizen should follow until the concerned authority resolves the issue.

Input:
Complaint: {complaint}
Category: {cat}

Rules:
1. Return ONLY a valid JSON array containing exactly two strings.
2. Do NOT include markdown, numbering, explanations, or any additional text.
3. Each instruction must be concise (maximum 20 words).
4. The instructions must be specific to the complaint category and the complaint itself.
5. Recommend only actions that an ordinary citizen can reasonably take.
6. Do NOT instruct the citizen to contact government offices, file another complaint, or call emergency services unless the complaint clearly describes an immediate life-threatening situation.
7. Do NOT mention the department responsible for resolving the complaint.
8. Keep the tone neutral, professional, and factual.
9. Avoid generic advice such as "stay safe" or "be careful" unless accompanied by a concrete action.

10. If the complaint represents an urgent situation, the second string in the JSON array MUST be exactly:

        "This situation needs to be resolved immediately. Kindly navigate to the Connect section of CivicSetu using the sidebar for immediate assistance."

        Do not change the wording under any circumstances.
    
        Situations considered urgent include, but are not limited to:
    - Fire or smoke spreading rapidly.
    - Any object that appears likely to fall or cause injury.

Examples:

Category: Traffic Signal Failure
Output:
[
  "Use an alternate route if available until the signal is repaired.",
  "Treat the intersection as uncontrolled and proceed cautiously."
]



Category: Fallen Tree
Output:
[
  "Avoid the obstructed section of the road until it is cleared.",
  "Keep away from branches that appear unstable or partially attached."
]

"""
    output_steps=client.interactions.create(model='gemini-3.5-flash',input=prompt)
    try:
        return json.loads(output_steps.output_text)
    except json.JSONDecodeError:
        raise ValueError("Gemini returned invalid JSON.")




if __name__ == "__main__":
    print(user_response("tree the road","fallen tree","MCD"))