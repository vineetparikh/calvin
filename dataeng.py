from github import Github

'''
Converts Github metadata into a vector of (num of)
[stars, contributors, commits, branches, closed issues, open issues, PRs, releases, forks, watchers]
Accepts info in the form "org name/repo name". For instance, "numpy/numpy".
'''
g = Github("vineetparikh","POMDPx12") # this would be filled in with credentials

def convert_number_to_value(number):
    if(number==1):
        return "Good"
    else:
        return "Bad"

def convert_value_to_number(value):
    if(value=="Good"):
        return 1
    else:
        return 0

def vectorize_from_github_name(orgrepo):
    repo = g.get_repo(orgrepo)

    # number of stars
    stars = repo.stargazers_count

    # number of public contributors
    contrib = repo.get_contributors().totalCount

    # number of commits
    commits = repo.get_commits().totalCount

    # number of branches
    branches = repo.get_branches().totalCount

    # number of closed issues
    closed_issues = repo.get_issues(state='closed').totalCount

    # number of open issues
    open_issues = repo.get_issues(state='open').totalCount

    # number of PRs
    prs = repo.get_pulls(base='master').totalCount

    # number of releases
    releases = repo.get_releases().totalCount

    # number of forks
    forks = repo.get_forks().totalCount

    # watcher count
    wat = repo.get_watchers().totalCount

    return [stars, contrib, commits, branches, closed_issues, open_issues, prs, releases, forks, wat]
