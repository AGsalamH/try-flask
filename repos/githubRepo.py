class GithubRepo:
    def __init__(self, name, language, stars):
        self.name = name
        self.language = language
        self.stars = stars

    def __str__(self):
        return f"-> {self.name} is a {self.language} repo with {self.num_stars} stars."

    def __repr__(self):
        return f"GithubRepo({self.name}, {self.language}, {self.num_stars})"