# CVT

> A minimal Computer Vision project template powered by uv.

## Features

- ⚡ Modern Python project with `uv`
- 🧠 PyTorch ready
- 👁️ OpenCV ready
- 📁 Clean project structure
- 🚀 Ready for Computer Vision projects

## Project Structure

```text
.
├── data/
│   ├── raw/
│   └── processed/
│
├── outputs/
│   ├── checkpoints/
│   └── predictions/
│
├── src/
│   ├── dataset.py
│   ├── model.py
│   └── utils.py
│
├── train.py
├── evaluate.py
├── predict.py
│
├── pyproject.toml
├── uv.lock
├── .python-version
├── .gitignore
└── README.md
```

## Getting Started

Clone the repository:

```bash
git clone https://github.com/rynzh/cvt.git
cd cvt
```

Install dependencies:

```bash
uv sync
```

Run:

```bash
uv run train.py
```

## Create a New Project

Using GitHub Template:

- Click **Use this template**
- Create a new repository

Or using `degit`:

```bash
degit rynzh/cvt [my-project]
code [my-project]

git init
git add .
git commit -m "chore: init"

uv sync
```

## Philosophy

This template intentionally stays minimal.

It provides only the common foundation shared by most Computer Vision projects:

- project structure
- dependency management
- environment management
- entry scripts

Everything else should be added only when the project actually needs it.

## License

MIT
