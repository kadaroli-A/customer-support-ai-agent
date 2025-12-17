# actions.py

def handle_action(intent, user_input, memory):
    """
    intent: detected user intent
    user_input: raw customer message
    memory: conversation history list
    """

    if intent == "greeting":
        return "Hello! How can I help you today?"

    elif intent == "order_status":
        return "Please share your order ID to check the status."

    elif intent == "refund":
        return "I can help with refunds. Can you tell me the order ID?"

    elif intent == "complaint":
        return "I'm sorry for the inconvenience. Let me escalate this to a human agent."

    else:
        return "I'm not sure I understood. Let me connect you to a human agent."