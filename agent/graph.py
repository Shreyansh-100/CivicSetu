from langgraph.graph import StateGraph,END
import os
from typing import List,TypedDict
from Agent_input import input_agent
from Agent_image import image_agent
from Agent_Routing import routing_agent
from Agent_Response import response_agent


class AgentState(TypedDict):

    complaint: str
    img_path:str
    cat:str
    dept:str
    ai_flag: bool
    conf_score :float
    verification:str
    priority:float
    label:str
    action:List
    user_response:List

def input(state: AgentState) ->AgentState:
    res=input_agent.output(state['complaint'])
    
    state['cat']=res['category']
    state['dept']=res['department']

    return state

def image_check(state:AgentState) -> AgentState:
    res=image_agent.output(state['img_path'],state['cat'])

    state['conf_score']=res['conf_score']
    state['ai_flag']=res['flag']

    return state

def route_complaint(state: AgentState) ->AgentState :
    res= routing_agent.route_complaint(
        state['complaint'],
        state['cat'],
        state['dept'],
        state['ai_flag'],
        state['conf_score']
    )

    state['verification']=res['verification']
    state['priority']=res['priority']
    state['label']=res['label']
    state['action']=res['recommend_actions']
    
    return state

def respond(state:AgentState) ->AgentState :
    res=response_agent.user_response(
        state['complaint'],
        state['cat'],
        state['dept']
    )
    state['user_response']=res
    return state

graph=StateGraph(AgentState)
graph.add_node("input",input)
graph.add_node("image",image_check)
graph.add_node("route_complaint",route_complaint)
graph.add_node("response",respond)

graph.set_entry_point("input")
graph.add_edge("input","image")
graph.add_edge("input","response")

graph.add_edge("image","route_complaint")

graph.add_edge("response",END)
graph.add_edge("route_complaint",END)



app=graph.compile()
res=app.invoke({"complaint":"fallen tree","img_path":"/mnt/c/Users/2.LAPTOP-GMFP48KM/Downloads/test1.jpg"})
print(res)



