import re
import json
from dataclasses import dataclass

@dataclass
class Response:
    response : str
    words : list[str]
    required_words : list[str]

class Chatbot:
    def __init__(self, name : str) -> None:
        self.name : str = name
        self.responses : list[Response] = self.__load_responses()
    
    @staticmethod
    def __load_responses() -> list[Response]:
        responses : list[Response] = list()
        
        with open("responses.json", "r") as file:
            for response in json.load(file):
                responses.append(Response(
                    response["response"],
                    response["words"],
                    response["required_words"]
                ))
        
        return responses
    
    @staticmethod
    def __match_rating(text : str, response : Response) -> float:
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
    
    def display_welcome(self) -> None:
        print(f"\nWelcome, I am {self.name} the Chatbot at your assistance.")
    
    def get_response(self, prompt : str) -> str:
        matches : dict[str, float] = dict()
        
        for response in self.responses:
            matches.setdefault(response.response, self.__match_rating(prompt, response))
        
        best_match : str = max(matches, key=matches.get) # type: ignore
        
        if matches[best_match] == 0:
            return "I don't understand... [0%]"
        else:
            return f"{best_match} [{matches[best_match]:.0%}]"


def split_text(text : str) -> list[str]:
    return re.split(r"\s+|[,;?!.-]\s*", text.lower())

def main() -> None:
    Nina : Chatbot = Chatbot("Nina")
    Nina.display_welcome()
    
    while True:
        user_input : str = input("\nYou: ")
        chatbot_output : str = Nina.get_response(prompt=user_input)
        
        print(f"Bot: {chatbot_output}")

if __name__ == "__main__":
    main()