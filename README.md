# LLM-models-playground

This is a Python project for experimenting with LLM models.

## Prerequisites

This project uses [UV](https://github.com/astral-sh/uv) as the Python package manager and environment manager. UV is a fast, reliable Python package installer and resolver written in Rust.

**Alternative:** You can also use Anaconda to run the Jupyter notebooks if you prefer. This project includes an `environment.yml` file that you can use with Anaconda/Miniconda.

### Installing UV

To install UV, run one of the following commands:

**On macOS and Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**On Windows (PowerShell):**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Using pip:**
```bash
pip install uv
```

**Using Homebrew (macOS):**
```bash
brew install uv
```

## Setup

To set up the project environment and install all dependencies, run:

```bash
uv sync
```

This will:
- Create a virtual environment (if it doesn't exist)
- Install all project dependencies
- Make the project ready to run Python scripts and Jupyter notebooks

## Usage

After running `uv sync`, you can run Python files and Jupyter notebooks using:

```bash
uv run python your_script.py
```

or to start Jupyter:

```bash
uv run jupyter lab
```

### Using Anaconda (Alternative)

If you prefer to use Anaconda instead of UV, you can set up the environment using:

```bash
conda env create -f environment.yml
conda activate llm-models-playground
jupyter lab
```

This will create a conda environment with all the required dependencies and allow you to run the Jupyter notebooks.
