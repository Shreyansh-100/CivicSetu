import ast
import json
import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
class routing_agent():

    def type_verify(flag,conf_score):
        if(flag==True or conf_score<0.5):
            return "Manual Verification needed"
        else:
            return "Verified"



    def recommend_action(complaint,cat,dept):
        api_key=os.getenv("Gemini")
        if not api_key:
            raise ValueError("Key not found")
        
        client=genai.Client(api_key=api_key)
        
        prompt=f"""
    You are generating field instructions for a Delhi civic grievance routing system.

    Return exactly one JSON array with exactly 3 strings. No markdown, no numbering,
    no explanation, no extra text.

    Each string must be one concrete operational step for the assigned department.
    Avoid vague wording such as "look into it", "take necessary action",
    "resolve the issue", "coordinate with authorities", or "ensure public safety"
    unless you also name the exact action.

    Rules:
    - Use the complaint details directly: location, object, and hazard.
    - Do not change the assigned department.
    - Do not suggest public awareness campaigns, long-term policy, or generic review.
    - Step 1 should secure/inspect the specific spot.
    - Step 2 should perform the category-specific fix.
    - Step 3 should verify completion and clear the area.

    Category-specific examples:
    - Fire Incident: dispatch fire tender, isolate area, extinguish flames/smoke source.
    - Electricity Problem: isolate power, repair exposed/sagging/sparking cable or box.
    - Illegal Hawking and Encroachment: remove unauthorized stalls/carts and clear footpath.
    - Illegal Parking: tow/challan blocking vehicles and restore traffic flow.

    Following is the input:-
    Complaint: {complaint}
    Category: {cat}
    Department: {dept}
    """
        output_action=client.interactions.create(model='gemini-3.5-flash',input=prompt)
        try:
            return json.loads(output_action.output_text)
        except json.JSONDecodeError:
            raise ValueError("Gemini returned invalid JSON.")

    def calulate_priority(cat,conf_score,flag):
        
        if(routing_agent.type_verify(flag,conf_score)=="Manual Verification needed"):
            return 0.5
        high=["fire","tree","traffic","water","electricity"]
        moderate=["sewage","garbage","parking","construction"]
        low=["enroachment","animals"]

        cat=cat.lower()
        for h in high:
            if h in cat:
                return conf_score*1
        for m in moderate:
            if m in cat:
                return conf_score*0.9
            
        for l in low:
            if l in cat:
                return conf_score*0.75
            
    def priority_label(priority):
        if(priority>=0.8):
            return 'High'
        elif(priority >=0.6):
            return 'Moderate'
        else:
            return 'Low'

    def route_complaint(complaint:str, cat:str, dept:str, flag:bool, conf_score:float):

        verification = routing_agent.type_verify(flag, conf_score)

        priority = routing_agent.calulate_priority(cat, conf_score, flag)
        
        label=routing_agent.priority_label(priority)

        actions = routing_agent.recommend_action(complaint, cat, dept)

        return {
            "verification": verification,
            "priority": priority,
            "label":label,
            "recommended_actions": actions
        }

 
