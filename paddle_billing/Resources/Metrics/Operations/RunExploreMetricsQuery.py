from dataclasses import dataclass

from paddle_billing.Resources.Metrics.Operations.ExploreMetrics import (
    ExploreFilter,
    ExploreMeasure,
    ExploreMetrics,
    ExploreOrderBy,
)

__all__ = ["ExploreFilter", "ExploreMeasure", "ExploreOrderBy", "RunExploreMetricsQuery"]


@dataclass
class RunExploreMetricsQuery(ExploreMetrics):
    """
    Deprecated: Use ExploreMetrics with Client.metrics.explore() instead.
    """
