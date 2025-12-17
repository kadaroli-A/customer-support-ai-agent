# main.py
# Customer Support AI Agent (CLI Version)

# -------------------------------
# Step 1: Escalation keywords
# -------------------------------
ESCALATION_KEYWORDS = [
    "complaint",
    "legal",
    "lawyer",
    "refund",
    "cancel",
    "sue",
    "angry",
    "manager",
    "human",
    "escalate"
]

# -------------------------------
# Step 2: Escalation check function
# -------------------------------
def check_escalation(user_input):
    user_input = user_input.lower()
    for word in ESCALATION_KEYWORDS:
        if word in user_input:
            return True
    return False


# -------------------------------
# Step 3: Memory (simple list)
# -------------------------------
conversation_memory = []


# -------------------------------
# Step 4: Intent detection
# -------------------------------
def detect_intent(user_input):
    text = user_input.lower()

    if any(word in text for word in ["hi", "hello", "hey"]):
        return "greeting"
    elif "order" in text:
        return "order_status"
    elif "refund" in text:
        return "refund"
    elif "complaint" in text or "problem" in text:
        return "complaint"
    else:
        return "unknown"


# -------------------------------
# Step 5: Escalation decision
# -------------------------------
def should_escalate(intent):
    return intent in ["complaint", "unknown"]


# -------------------------------
# Step 6: Main execution loop
# -------------------------------
def main():
    print("🤖 Customer Support AI Agent")
    print("Type 'exit' to quit\n")

    while True:
        user_input = input("Customer: ")

        # Exit condition
        if user_input.lower() in ["exit", "quit"]:
            print("AI: Thank you for contacting support. Goodbye!")
            break

        # Store user input in memory
        conversation_memory.append(f"Customer: {user_input}")

        # Step 6.1: Escalation by keyword
        if check_escalation(user_input):
            print("AI: This looks serious. Connecting you to a human support agent now.")
            conversation_memory.append("AI: Escalated to human agent.")
            break

        # Step 6.2: Intent detection
        intent = detect_intent(user_input)

        # Step 6.3: Normal AI reply
        ai_reply = f"I understand your concern about '{intent}'. Let me help you."
        print("AI:", ai_reply)
        conversation_memory.append(f"AI: {ai_reply}")

        # Step 6.4: Escalation by intent
        if should_escalate(intent):
            print("⚠️ Escalation: Issue requires human support.")
            conversation_memory.append("AI: Escalated due to intent.")
            break


# -------------------------------
# Program entry point
# -------------------------------
if __name__ == "__main__":
    main()