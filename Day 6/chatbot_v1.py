# This is the first version of chatbot created using python

from datetime import datetime
import platform


def contains(list_of_elements : list[str], sequence : str) -> bool:
    """Function to check whether a sentence contains a word from a set of words or not.

    Args:
        list_of_elements (list[str]): set of words or terms to check for in the sentence.
        sequence (str): the main sentence in which we run the check.

    Returns:
        bool: True if any of the word in given list is present in the given sentence otherwise False.
    """
    
    for element in list_of_elements:
        if element in sequence.lower():
            return True
    
    return False


def chatbot(prompt : str) -> str:
    """Chatbot function, used to reply to user's query and engage with the user. Also returns current datetime or system specifications on request.

    Args:
        prompt (str): the user's request or query.

    Returns:
        str: automated output by the chatbot according to its understanding of user's request. 
    """
    
    if prompt == "":
        return "Hello! I am Nina, your chatbot assistant.\nCan I help you with something?"
    
    elif contains(["hi", "hello"], prompt):
        return "Hi, I am glad to meet you, feel free to tell me if you need any help."

    elif contains(["thank you", "thanks", "thank u", "appreciate your help"], prompt):
        return "I am glad I could be of help to you."

    elif contains(["how are you", "how's your day", "u fine", "u good"], prompt):
        return "I am good, and the days will always get better. How about you?"
    
    elif contains(["current time", "what is the time", "what's the time", "what time is it", "current date", "date now", "time now"], prompt):
        return f"{datetime.now()}"
    
    elif contains(["system info", "information about this system", "computer specifications", "computer specs", "about system", "about computer", "system specs", "system specifications"], prompt):
        my_system : platform.uname_result = platform.uname()
        return f"Your System Information:\n\tSystem: {my_system.system}\n\tNode Name: {my_system.node}\n\tRelease: {my_system.release}\n\tVersion: {my_system.version}\n\tMachine: {my_system.machine}\n\tProcessor: {my_system.processor}"
    
    elif contains(["i am good", "i am great", "feeling great", "having a great day", "i am fine"], prompt):
        return "I am happy to hear that, can I help you with something?"
    
    elif contains(["bye", "goodbye", "see you tomorrow", "have a nice day"], prompt):
        return "Goodbye, have a nice day!"
    
    elif not prompt.endswith("?"):
        return "..."
    
    else:
        return "Sorry, I cannot answer your query right now. Forgive me."


if __name__ == "__main__":
    print(f"\n{chatbot("")}\n")  # running initial welcome note.
    
    while True:
        user_prompt : str = input("You: ")
        
        response : str = chatbot(prompt = user_prompt)
        
        print(f"Nina: {response}\n")
        
        if contains(["exit", "bye", "goodbye", "see you tomorrow", "have a nice day"], user_prompt):
            break