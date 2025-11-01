# Autonomous Lane Assist System

This repository contains refactored code from simple scripts into a small
Python package. It provides lane detection utilities and basic image
operations using OpenCV and NumPy.

Installation (using Poetry):

1. Install poetry (https://python-poetry.org/) if you don't have it.
2. From the project root run:

```bash
poetry install
poetry shell
python -m autonomous_lane_assist_system.lanekeeping
```

Notes:
- The original project used RPi.GPIO. The package will still import on
  non-Raspberry Pi machines. To run the camera loop with GPIO control set
  use_gpio=True when calling `run_camera_loop` and run on a Pi with the
  RPi.GPIO package installed.
- The package exposes:
  - `autonomous_lane_assist_system.lanekeeping` – lane detection and camera loop
  - `autonomous_lane_assist_system.image_ops` – small image helpers

Authors
-------

Primary author:

- SubhadipDas123 <127828935+SubhadipDas123@users.noreply.github.com>

Publishing to PyPI
------------------

Manual publish (local):

1. Ensure you have an API token created on PyPI (Account -> API tokens) and set it to an environment variable or use `twine` by passing username/password.
2. Build the distributions:

```bash
python3 -m build
```

3. Upload with twine:

```bash
python3 -m pip install --user --upgrade twine
python3 -m twine upload dist/*
```

Automated publish (GitHub Actions):

- The repository includes `.github/workflows/publish.yml` which publishes on tag pushes (tags starting with `v`). To enable it, create a repository secret named `PYPI_API_TOKEN` containing a PyPI API token with appropriate scope.

