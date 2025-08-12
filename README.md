# sonarcloud-demo-python
Small, intentionally vulnerable Python example for SonarCloud.

## Files
- `app.py` – contains several obvious security issues for demo purposes.
- `requirements.txt` – only stdlib used; kept empty.
- `sonar-project.properties` – optional (works with SonarCloud GitHub Action). Not required for Automatic Analysis.

## Quick use (zero install, SonarCloud Automatic Analysis)
1) Create a **public** GitHub repo and upload these files.
2) Go to **sonarcloud.io** → sign in with GitHub → **Create project** → import your repo.
3) In the project, enable **Automatic Analysis**.
4) Once the analysis completes, open **Issues → Vulnerabilities**, take a screenshot.

> If Automatic Analysis is unavailable for your setup, use GitHub Actions with SonarCloud and keep this `sonar-project.properties` as-is (replace placeholders).
