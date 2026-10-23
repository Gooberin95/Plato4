# The Copper Latitude

A fictional travel journal for Inez Marlow, set in Reflex. Issue 07, *Between Stations*, is a magazine on a dark canvas: dispatches you can open one by one, an atlas you can filter by continent, and a field kit you can tick off in the browser.

The painting behind every page is the shared canvas for this project. It is served from `assets/background.jpg` and applied once, on the root of the page, with `background_size="cover"`, `background_position="center"`, and `background_attachment="fixed"`.

## Python

This site targets **CPython 3.14.4**.

[Reflex 0.10.0](https://pypi.org/project/reflex/0.10.0/) supports it. That release requires Python `>=3.11,<4`, and Python 3.14 support has been in Reflex since 0.8.15. `.python-version` is pinned to `3.14.4`.

Ubuntu’s `python3` is not 3.14. The deadsnakes `python3.14` package currently tracks a newer 3.14 patch, so the steps below install **3.14.4** itself and then create the virtual environment with `python3.14`.

## Run on Ubuntu

Install Python 3.14.4 if `python3.14 --version` does not already print `Python 3.14.4`:

```bash
sudo apt-get update
sudo apt-get install -y curl ca-certificates
curl -LsSf https://astral.sh/uv/install.sh | sh
source "$HOME/.local/bin/env"
uv python install 3.14.4
python3.14 --version
```

Clone the repo, install Reflex, and start the app:

```bash
git clone https://github.com/Gooberin95/Plato4.git
cd Plato4
python3.14 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

`reflex init` is only needed if `rxconfig.py` and the `copper_latitude` package are missing. They are already in this repository, so skip it:

```bash
# reflex init
reflex run
```

Open [http://localhost:3000](http://localhost:3000).

The first `reflex run` downloads Reflex’s frontend toolchain and compiles the app. That can take a few minutes. Leave the terminal open while you read. Stop the server with Ctrl+C.

The backend listens on port 8000. The site you open is the frontend on port 3000.

Fraunces and Newsreader load from Google Fonts, with Palatino and Georgia as the offline fallbacks.

## Deploying to Azure

The GitHub Actions workflow builds this site on every push to `main`. Deploying to Azure App Service is described in [DEPLOY.md](DEPLOY.md). Those deploy jobs stay skipped until an Azure subscription exists and the variable `AZURE_DEPLOY_ENABLED` is set to `true`.

## Pages

| Path | What it is |
| --- | --- |
| `/` | Issue opener: masthead, lead dispatch, and the rest of the contents |
| `/dispatches` | The dispatch book |
| `/dispatches/[slug]` | One essay per URL |
| `/atlas` | Destinations, filtered by continent |
| `/kit` | Packing list you can tick off for this browser session |
| `/about` | Colophon: who Inez is, and that she is fictional |
