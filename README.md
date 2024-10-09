# Github Activity
This Python script fetches and displays the latest GitHub events for a specified user. It is a solution for the [GitHub User Activity project](https://roadmap.sh/projects/github-user-activity).

## Prerequisites
- Python 3.x
- [uv](https://github.com/astral-sh/uv) (For package management and venv)

## Installation
- Clone the repository:
    ```bash
    git clone https://github.com/pixdump/github-activity.git
    cd github-activity
    ```
<details> <summary>Using uv</summary>

- To install requirements

    ```bash
    uv sync
    ```
- To Run the Script

    ```bash
    uv run python gh-activivty.py <username>
    ```
</details>

<details> <summary>Using pip</summary>


- Create a virtual environment:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```
- Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

- Usage: Run the script with the desired GitHub username:
    ```bash
    python3 gh-activity.py <username>
    ```

</details>


