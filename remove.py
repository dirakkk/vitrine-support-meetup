import requests

# Remplacez par votre token d'accès personnel
TOKEN = ''
# Remplacez par le nom de votre dépôt et le propriétaire
OWNER = 'dirakkk'
REPO = 'vitrine-next'

# URL de base pour l'API de GitHub
BASE_URL = f'https://api.github.com/repos/{OWNER}/{REPO}/actions/runs'

# En-têtes pour les requêtes
headers = {
    'Authorization': f'token {TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

# Fonction pour obtenir tous les workflows runs
def get_workflow_runs():
    runs = []
    page = 1
    while True:
        response = requests.get(BASE_URL, headers=headers, params={'per_page': 100, 'page': page})
        if response.status_code != 200:
            raise Exception(f"Erreur lors de la récupération des workflows runs: {response.status_code}")
        data = response.json()
        if not data['workflow_runs']:
            break
        runs.extend(data['workflow_runs'])
        page += 1
    return runs

# Fonction pour supprimer un workflow run
def delete_workflow_run(run_id):
    url = f'{BASE_URL}/{run_id}'
    response = requests.delete(url, headers=headers)
    if response.status_code != 204:
        raise Exception(f"Erreur lors de la suppression du workflow run {run_id}: {response.status_code}")

# Obtenir tous les workflows runs
workflow_runs = get_workflow_runs()

# Supprimer chaque workflow run
for run in workflow_runs:
    run_id = run['id']
    print(f"Suppression du workflow run {run_id}...")
    delete_workflow_run(run_id)
    print(f"Workflow run {run_id} supprimé.")

print("Tous les workflows runs ont été supprimés.")