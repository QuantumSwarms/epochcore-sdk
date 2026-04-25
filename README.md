# epochcore-sdk

> Public client SDK for the **EpochCore** platform — a thin wrapper around the EpochCore zero-latency single-API agent surface.

[![PyPI](https://img.shields.io/badge/pypi-coming--soon-lightgrey)]() [![License](https://img.shields.io/badge/license-Apache--2.0-blue)](LICENSE) [![Status](https://img.shields.io/badge/status-pre--alpha-orange)]()

## Install

```bash
pip install epochcore-sdk  # (coming soon)
```

For now, install from source:

```bash
git clone https://github.com/QuantumSwarms/epochcore-sdk
cd epochcore-sdk
pip install -e .
```

## Quickstart

```python
from epochcore_sdk import EpochCore

ec = EpochCore(api_key="...")  # or env: EPOCHCORE_API_KEY

# Resolve a D-KaP pixel tensor by content address
tensor = ec.dkap.get("dkap://identity/0xabc123")

# Dispatch an agent skill
result = ec.agents.run("hydro", inputs={"basin": "Catawba"})

print(result)
```

## Modules

| Module | Purpose |
|---|---|
| `epochcore_sdk.dkap` | Decentralized Knowledge as Pixels client |
| `epochcore_sdk.agents` | Agent runtime dispatch (zero-latency single API) |
| `epochcore_sdk.epochpay` | Payment + billing-evidence client |
| `epochcore_sdk.epochcoverage` | Coverage / attestation helpers |
| `epochcore_sdk.watermark` | Quantum watermark verification |

## Layout

```
.
├── src/
│   └── epochcore_sdk/
│       └── __init__.py
├── examples/
├── tests/
├── pyproject.toml
└── LICENSE
```

## Status

Pre-alpha public surface. Proprietary platform internals remain in private EpochCore infrastructure. Schema and API subject to change.

## Related

- [`epochcore-dkap-spec`](https://github.com/QuantumSwarms/epochcore-dkap-spec) — the D-KaP specification
- [`epochcore-docs`](https://github.com/QuantumSwarms/epochcore-docs) — platform documentation

## License

[Apache License 2.0](LICENSE) © EpochCore LLC.
