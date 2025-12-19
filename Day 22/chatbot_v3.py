import re
import json
from dataclasses import dataclass

@dataclass
class Response:
    response : str
    words : list[str]
    required_words : list[str]


def load_responses() -> list[Response]:
    responses : list[Response] = list()
    
    with open("responses.json", "r") as file:
        for response in json.load(file):
            responses.append(Response(
                response["response"],
                response["words"],
                response["required_words"]
            ))
    
    return responses

def split_text(text : str) -> list[str]:
    return re.split(r"\s+|[,;?!.-]\s*", text.lower())

def match_rating(text : str, response : Response) -> float:
    text = text.lower()
    score : int = 0
    has_required_words : bool = True
    
    for required_word in response.required_words:
        if required_word not in text:
            has_required_words = False
            break
    
    if has_required_words:
        for word in split_text(text):
            if word in response.words:
                score += 1
        
        percent_matched : float = score / len(response.words)
        return percent_matched
    else:
        return 0

def get_response(prompt : str, responses : list[Response]) -> str:
    matches : dict[str, float] = dict()
    
    for response in responses:
        matches.setdefault(response.response, match_rating(prompt, response))
    
    best_match : str = max(matches, key=matches.get) # type: ignore
    
    if matches[best_match] == 0:
        return "I don't understand... [0%]"
    else:
        return f"{best_match} [{matches[best_match]:.0%}]"

def main() -> None:
    responses : list[Response] = load_responses()
    
    print("\nWelcome, I am Nina the Chatbot at your assistance.")
    while True:
        user_input : str = input("\nYou: ")
        chatbot_output : str = get_response(prompt=user_input, responses=responses)
        
        print(f"Bot: {chatbot_output}")

if __name__ == "__main__":
    main()