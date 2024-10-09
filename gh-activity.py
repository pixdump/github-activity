import sys
import requests
from rich import print as rprint

def get_user_activity(username: str):
    url = f"https://api.github.com/users/{username}/events"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        latest_events = response.json()
        rprint(f"Latest events for [bold green]{username}[/bold green]:")
        for event in latest_events:
            if event['type'] == 'PushEvent':
                rprint(f"{username} pushed to {event['repo']['name']}")

            elif event['type'] == 'IssuesEvent':
                action = event['payload']['action'].capitalize()
                repo_name = event['repo']['name']
                issue_number = event['payload']['issue']['number']
                issue_url = f"https://github.com/{repo_name}/issues/{issue_number}"
                rprint(f"{username} {action} an issue in [bold]{repo_name}[/bold]: [link={issue_url}]{issue_url}[/link]")

            elif event['type'] == 'WatchEvent':
                rprint(f"{username} starred {event['repo']['name']}")
            elif event['type'] == 'PullRequestEvent':
                rprint(f"{username} created pull request at {event['payload']['pull_request']['html_url']}")
            elif event['type'] == 'CreateEvent':
                ref_type = event['payload']['ref_type']
                repo_name = event['repo']['name']
                if ref_type == 'repository':
                    repo_url = event['repo']['url'].replace("api.github.com", "github.com").replace("repos/", "")
                    rprint(f"{username} created a repository [link={repo_url}]{repo_name}[/link]: {event['payload']['description']}")
                else:
                    ref_name = event['payload']['ref']
                    rprint(f"{username} created a {ref_type} '{ref_name}' in [bold]{repo_name}[/bold]")
            elif event['type'] == 'IssueCommentEvent':
                comment_id = event['payload']['comment']['id']  # Get the comment ID
                issue_number = event['payload']['issue']['number']
                repo_name = event['repo']['name']
                comment_url = f"https://github.com/{repo_name}/issues/{issue_number}#issuecomment-{comment_id}"
                
                rprint(f"{username} commented on issue [bold]{issue_number}[/bold] in [bold]{repo_name}[/bold]: [link={comment_url}]{comment_url}[/link]")

            else:
                rprint(f"Other Eventtype:{event['type']}")
    except requests.exceptions.HTTPError as err:
        if response.status_code == 404:
            rprint(f"[red]Error 404: User '{username}' not found[/red]")
        else:
            rprint(f"Error fetching events for {username}: {response.status_code} - {err}")
    except requests.exceptions.RequestException as err:
        rprint(f"Request error for {username}: {err}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        get_user_activity(sys.argv[1])
    else:
        rprint("[yellow]Please provide a gitHub username[/yellow]")
