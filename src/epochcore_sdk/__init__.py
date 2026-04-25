"""epochcore_sdk — public client SDK for the EpochCore platform.

This is a pre-alpha public surface. Proprietary platform internals remain in
private EpochCore infrastructure.
"""
from __future__ import annotations

__version__ = "0.0.1"
__all__ = ["EpochCore", "__version__"]

import os
from dataclasses import dataclass, field
from typing import Any, Optional


@dataclass
class EpochCore:
    """Top-level client for the EpochCore zero-latency single-API surface."""

    api_key: Optional[str] = None
    base_url: str = "https://api.epochcoreqcs.com"
    _extra: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if self.api_key is None:
            self.api_key = os.environ.get("EPOCHCORE_API_KEY")
        self.dkap = _DKaP(self)
        self.agents = _Agents(self)
        self.epochpay = _EpochPay(self)
        self.epochcoverage = _EpochCoverage(self)
        self.watermark = _Watermark(self)


@dataclass
class _Namespace:
    client: "EpochCore"


class _DKaP(_Namespace):
    def get(self, address: str) -> dict[str, Any]:  # pragma: no cover
        raise NotImplementedError("pre-alpha: stub")


class _Agents(_Namespace):
    def run(self, skill: str, inputs: dict[str, Any]) -> dict[str, Any]:  # pragma: no cover
        raise NotImplementedError("pre-alpha: stub")


class _EpochPay(_Namespace):
    pass


class _EpochCoverage(_Namespace):
    pass


class _Watermark(_Namespace):
    def verify(self, tensor: bytes, signature: bytes) -> bool:  # pragma: no cover
        raise NotImplementedError("pre-alpha: stub")
