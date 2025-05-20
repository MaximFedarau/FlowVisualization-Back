# FlowVisualization (Backend)

Flow Visualization is a handy tool that allows you to visually see how algorithms for finding the maximum flow in a graph work.

Here's an example of the Ford-Fulkerson algorithm visualization (the dotted lines are the edges of the graph, and the solid lines are the edges of some extending path)

[Test](https://github.com/user-attachments/assets/f5898b98-52e6-4943-b277-69879973e5b1)

## Our Stack

```json
{
  "dependencies": {
    "fastapi": "0.115.12", 
    "pydantic": "2.11.4",
    "pydantic_core": "2.33.2",
    "cloudinary": "1.44.0",
    "manim": "0.19.0",
  },
  "devDependencies": {
    "ruff": "0.11.8",
    "pytest": "8.3.5",
    "coverage": "7.8.0",
    "mypy": "1.15.0",
    "pydantic-settings": "2.9.1",
    "python-dotenv": "1.1.0",
  }
}
```

## How to run this project

1) [Install manim.](https://docs.manim.community/en/stable/installation.html)
2) Install dependencies: `pip install -r requirements.txt`.
3) Add [Cloudinary](https://cloudinary.com/) environment variables to `.env` file. Required variables are specified in `app/config.py` file. Their values you can find on your dashboard in your personal Cloudinary account.
4) Run in development mode with `fastapi dev main.py` or in production mode with `fastapi run main.py`.
5) Run tests with `./scripts/test.sh`.
6) Run lint with `./scripts/lint.sh`.
7) Run formatting with `./scripts/format.sh`.

## Our Team

Maxim Fedarau (@MaximFedarau):
- Wrote this `README.md`😇.
- Set up CI, working environment and project tests.
- Was responsible for Manim features.

Akimov Daniil (@akimovdaniil):
- Wrote all the project algorithms.
- Wrote graph generation.
