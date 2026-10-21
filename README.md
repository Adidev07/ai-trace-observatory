# AI Trace Observatory

Inspect synthetic AI request traces, calculate service metrics, and detect threshold breaches without an external telemetry service.

AI-assisted learning project with synthetic data. No paid API, hosted model, or external dependency required.

## Run

Requires Python 3.10+.

```sh
python server.py
```

Open http://127.0.0.1:8000. Alternative port: `python server.py --port 8001`. On Windows, `py` can replace `python`. Stop with Ctrl+C.

## Test

```sh
python -m unittest discover -v
```

## Detailed documentation

Read [PROJECT_GUIDE.pdf](PROJECT_GUIDE.pdf) for architecture, file responsibilities, algorithms, API examples, limits, demo instructions, GitHub setup and interview preparation. The same guide is available as editable [GUIDE.md](GUIDE.md).

## Demo

AI features need operational visibility beyond whether one response looks good. This dashboard reads four synthetic request traces and calculates request count, error rate, tail latency, token use and illustrative cost. Run with model all, then demo-small. Lower the latency threshold to create more alerts. Explain that the dashboard replays fixture data and does not instrument a live model.

## Limits

Local single-process demo; no authentication. Use synthetic inputs. Do not expose the development server publicly. Rules and fixture-based metrics do not establish real model quality.

## Make it yours

Run it, inspect the code, replace fixtures with your own public examples and implement a documented improvement. Explain which parts were AI-assisted and what you changed.

## License

MIT; see LICENSE.
