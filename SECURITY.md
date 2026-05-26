# Security Notes

This project has a basic security check in the CI/CD pipeline.

## Image scan

The Docker image is scanned with Trivy in GitHub Actions.

The scan checks for:

`HIGH,CRITICAL`

For this project, Trivy only reports the result:

`exit-code: "0"`

This means the pipeline does not fail automatically if Trivy finds an issue. I used this mode because this is a case project and I wanted to see the scan result first.

## Container image

The Docker image is pushed to GitHub Container Registry:

`ghcr.io/alperennozalp/fastapi-devops-pipeline:latest`

The package is public so it can be pulled easily during review and local Kubernetes testing.

## Secrets

The workflow uses GitHub's default token:

`${{ secrets.GITHUB_TOKEN }}`

I did not add any custom secret value to the repository.

## If a secret is exposed

If a token or secret is accidentally shared, these steps can be followed:

1. Delete or disable the old token.
2. Create a new token if it is still needed.
3. Add the new token again from GitHub repository settings.
4. Run the GitHub Actions workflow again.
5. Check that the pipeline still works.

## Possible improvements

In the future, this project can be improved by:

- Failing the pipeline when serious vulnerabilities are found.
- Adding dependency scanning.
- Adding branch protection rules for the `main` branch.