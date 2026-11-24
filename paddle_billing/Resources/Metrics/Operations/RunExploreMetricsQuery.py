from dataclasses import dataclass

from paddle_billing.Resources.Metrics.Operations.ExploreMetrics import (
    ExploreFilter as ExploreFilter,
    ExploreMeasure as ExploreMeasure,
    ExploreMetrics as ExploreMetrics,
    ExploreOrderBy as ExploreOrderBy,
)

__all__ = ["ExploreFilter", "ExploreMeasure", "ExploreOrderBy", "RunExploreMetricsQuery"]


@dataclass
class RunExploreMetricsQuery(ExploreMetrics):
    """
    Deprecated: Use ExploreMetrics with Client.metrics.explore() instead.
    """
