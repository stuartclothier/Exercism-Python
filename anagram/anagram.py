def find_anagrams(word: str, candidates: list[str]) -> list[str]:
    return [candidate for candidate in candidates 
            if sorted(word.lower()) == sorted(candidate.lower())
            and word.lower() != candidate.lower()]