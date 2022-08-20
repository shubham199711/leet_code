import re
from typing import List

def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        paragraph = re.sub(r"[!?',;.]", " ", paragraph)
        words = paragraph.split(" ")
        banned = set(banned)  # type: ignore
        _ans = {}
        for word in words:
            word = word.strip()
            if word == "":
                continue
            if word not in banned:
                if _ans.get(word) is not None:
                    _ans[word] = _ans[word] + 1
                else:
                    _ans[word] = 1
        return max(_ans, key=_ans.get)  # type: ignore