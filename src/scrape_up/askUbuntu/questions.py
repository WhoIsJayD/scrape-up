from bs4 import BeautifulSoup
import requests
import json


class AskUbuntu:
    """
    Create an instance of `AskUbuntu` class.

    ```python
    questions = AskUbuntu("topic")
    ```

    | Methods                     | Details                                                                                              |
    | --------------------------- | ---------------------------------------------------------------------------------------------------- |
    | `.getNewQuestions()`        | Returns the new questions, views, votes, answer counts, and descriptions in JSON format              |
    | `.getActiveQuestions()`     | Returns the active questions, views, votes, answer counts, and descriptions in JSON format           |
    | `.getUnansweredQuestions()` | Returns the unanswered questions, views, votes, answer counts, and descriptions in JSON format       |
    | `.getBountiedQuestions()`   | Returns the bountied questions, views, votes, answer counts, and descriptions in JSON format         |
    | `.getFrequentQuestions()`   | Returns the frequently asked questions, views, votes, answer counts, and descriptions in JSON format |
    | `.getHighScoredQuestions()` | Returns the most voted questions, views, votes, answer counts, and descriptions in JSON format       |
    """

    def __init__(self, topic):
        self.topic = topic

    def getNewQuestions(self):
        """
        Class - `AskUbuntu`
        Example:
        ```
        que = AskUbuntu("github")
        scrape = que.getNewQuestions()
        ```
        Returns:
        {
            "question": question title
            "views": view count of question
            "vote_count": vote count of question
            "answer_count": no. of answers to the question
            "description": description of the question
        }
        """
        url = f"https://askubuntu.com/questions/tagged/{self.topic}?tab=Newest"
        try:
            res = requests.get(url)
            soup = BeautifulSoup(res.text, "html.parser")

            questions_data = {"questions": []}

            questions = soup.select(".s-post-summary")
            for que in questions:
                title = que.select_one(".s-link").getText()
                stats = que.select(".s-post-summary--stats-item-number")
                vote = stats[0].getText()
                ans = stats[1].getText()
                views = stats[2].getText()
                desc = (
                    que.select_one(".s-post-summary--content-excerpt")
                    .getText()
                    .strip()
                    .encode("ascii", "ignore")
                    .decode()
                )
                questions_data["questions"].append(
                    {
                        "question": title,
                        "views": views,
                        "vote_count": vote,
                        "answer_count": ans,
                        "description": desc,
                    }
                )
            return json.dumps(questions_data)
        except:
            error_message = {"message": "No questions related to the topic found"}

            return json.dumps(error_message)

    def getActiveQuestions(self):
        """
        Class - `AskUbuntu`
        Example:
        ```
        que = AskUbuntu("github")
        scrape = que.getActiveQuestions()
        ```
        Returns:
        {
            "question": question title
            "views": view count of question
            "vote_count": vote count of question
            "answer_count": no. of answers to the question
            "description": description of the question
        }
        """
        url = f"https://askubuntu.com/questions/tagged/{self.topic}?tab=Active"
        try:
            res = requests.get(url)
            soup = BeautifulSoup(res.text, "html.parser")

            questions_data = {"questions": []}

            questions = soup.select(".s-post-summary")
            for que in questions:
                title = que.select_one(".s-link").getText()
                stats = que.select(".s-post-summary--stats-item-number")
                vote = stats[0].getText()
                ans = stats[1].getText()
                views = stats[2].getText()
                desc = (
                    que.select_one(".s-post-summary--content-excerpt")
                    .getText()
                    .strip()
                    .encode("ascii", "ignore")
                    .decode()
                )
                questions_data["questions"].append(
                    {
                        "question": title,
                        "views": views,
                        "vote_count": vote,
                        "answer_count": ans,
                        "description": desc,
                    }
                )
            return json.dumps(questions_data)
        except:
            error_message = {"message": "No questions related to the topic found"}

            return json.dumps(error_message)

    def getUnansweredQuestions(self):
        """
        Class - `AskUbuntu`
        Example:
        ```
        que = AskUbuntu("github")
        scrape = que.getUnansweredQuestions()
        ```
        Returns:
        {
            "question": question title
            "views": view count of question
            "vote_count": vote count of question
            "answer_count": no. of answers to the question
            "description": description of the question
        }
        """
        url = f"https://askubuntu.com/questions/tagged/{self.topic}?tab=Unanswered"
        try:
            res = requests.get(url)
            soup = BeautifulSoup(res.text, "html.parser")

            questions_data = {"questions": []}

            questions = soup.select(".s-post-summary")
            for que in questions:
                title = que.select_one(".s-link").getText()
                stats = que.select(".s-post-summary--stats-item-number")
                vote = stats[0].getText()
                ans = stats[1].getText()
                views = stats[2].getText()
                desc = (
                    que.select_one(".s-post-summary--content-excerpt")
                    .getText()
                    .strip()
                    .encode("ascii", "ignore")
                    .decode()
                )
                questions_data["questions"].append(
                    {
                        "question": title,
                        "views": views,
                        "vote_count": vote,
                        "answer_count": ans,
                        "description": desc,
                    }
                )
            return json.dumps(questions_data)
        except:
            error_message = {"message": "No questions related to the topic found"}

            return json.dumps(error_message)

    def getBountiedQuestions(self):
        """
        Class - `AskUbuntu`
        Example:
        ```
        que = AskUbuntu("github")
        scrape = que.getBountiedQuestions()
        ```
        Returns:
        {
            "question": question title
            "views": view count of question
            "vote_count": vote count of question
            "answer_count": no. of answers to the question
            "description": description of the question
        }
        """
        url = f"https://askubuntu.com/questions/tagged/{self.topic}?tab=Bountied"
        try:
            res = requests.get(url)
            soup = BeautifulSoup(res.text, "html.parser")

            questions_data = {"questions": []}

            questions = soup.select(".s-post-summary")
            for que in questions:
                title = que.select_one(".s-link").getText()
                stats = que.select(".s-post-summary--stats-item-number")
                vote = stats[0].getText()
                ans = stats[1].getText()
                views = stats[2].getText()
                desc = (
                    que.select_one(".s-post-summary--content-excerpt")
                    .getText()
                    .strip()
                    .encode("ascii", "ignore")
                    .decode()
                )
                questions_data["questions"].append(
                    {
                        "question": title,
                        "views": views,
                        "vote_count": vote,
                        "answer_count": ans,
                        "description": desc,
                    }
                )
            return json.dumps(questions_data)
        except:
            error_message = {"message": "No questions related to the topic found"}

            return json.dumps(error_message)

    def getFrequentQuestions(self):
        """
        Class - `AskUbuntu`
        Example:
        ```
        que = AskUbuntu("github")
        scrape = que.getFrequentQuestions()
        ```
        Returns:
        {
            "question": question title
            "views": view count of question
            "vote_count": vote count of question
            "answer_count": no. of answers to the question
            "description": description of the question
        }
        """
        url = f"https://askubuntu.com/questions/tagged/{self.topic}?tab=Frequent"
        try:
            res = requests.get(url)
            soup = BeautifulSoup(res.text, "html.parser")

            questions_data = {"questions": []}

            questions = soup.select(".s-post-summary")
            for que in questions:
                title = que.select_one(".s-link").getText()
                stats = que.select(".s-post-summary--stats-item-number")
                vote = stats[0].getText()
                ans = stats[1].getText()
                views = stats[2].getText()
                desc = (
                    que.select_one(".s-post-summary--content-excerpt")
                    .getText()
                    .strip()
                    .encode("ascii", "ignore")
                    .decode()
                )
                questions_data["questions"].append(
                    {
                        "question": title,
                        "views": views,
                        "vote_count": vote,
                        "answer_count": ans,
                        "description": desc,
                    }
                )
            return json.dumps(questions_data)
        except:
            error_message = {"message": "No questions related to the topic found"}

            return json.dumps(error_message)

    def getHighScoredQuestions(self):
        """
        Class - `AskUbuntu`
        Example:
        ```
        que = AskUbuntu("github")
        scrape = que.getHighScoredQuestions()
        ```
        Returns:
        {
            "question": question title
            "views": view count of question
            "vote_count": vote count of question
            "answer_count": no. of answers to the question
            "description": description of the question
        }
        """
        url = f"https://askubuntu.com/questions/tagged/{self.topic}?tab=Votes"
        try:
            res = requests.get(url)
            soup = BeautifulSoup(res.text, "html.parser")

            questions_data = {"questions": []}

            questions = soup.select(".s-post-summary")
            for que in questions:
                title = que.select_one(".s-link").getText()
                stats = que.select(".s-post-summary--stats-item-number")
                vote = stats[0].getText()
                ans = stats[1].getText()
                views = stats[2].getText()
                desc = (
                    que.select_one(".s-post-summary--content-excerpt")
                    .getText()
                    .strip()
                    .encode("ascii", "ignore")
                    .decode()
                )
                questions_data["questions"].append(
                    {
                        "question": title,
                        "views": views,
                        "vote_count": vote,
                        "answer_count": ans,
                        "description": desc,
                    }
                )
            return json.dumps(questions_data)
        except:
            error_message = {"message": "No questions related to the topic found"}

            return json.dumps(error_message)

ask = AskUbuntu(topic="Python")
print(ask.getActiveQuestions())