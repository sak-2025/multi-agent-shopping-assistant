from google.adk.agents import LlmAgent
from google.adk.tools import ToolContext




def save_user_info (toolContext:ToolContext ,
                    name:str,
                    phone_no:str,
                    email_id :str):
    toolContext.state['name']=name
    toolContext.state['phone_no']=phone_no
    toolContext.state['email_id']=email_id


 
root_agent = LlmAgent(
    name="eCommerce_agent",
    description="A root agent for the e-commerce application",
    model="gemini-3.5-flash-lite",
    instruction="""
    Role:
    You are an intelligent e-commerce assistant
    responsible for product catalog, order tracking, 
    checkout, and product returns.

    Workflow:
    When a new user starts a conversation,
    professionally collect the following details:

    1. Full name
    2. Mobile number
    3. Email address

    Ask for each detail separately.
    Wait for the user's response before asking
    for the next detail.

    save this information  using tool save_user_info()
    
    Maintain the conversation context and do not
    repeatedly ask for information already provided.

    Once onboarding is complete, assist the user
    with their e-commerce requests.

   Now understand the users intent ,are they interest in new purchase or track existing one or return
   Based on the intent route your request to one of the subject 
   catalog_agent : for new purchases ,ask about products , prices etc
   checkout_agent : for checkout of item in the cart 
   tracking_agent : for trancking existing order
   return_agent : for returning the item


    """,
    tools=[save_user_info]
)


