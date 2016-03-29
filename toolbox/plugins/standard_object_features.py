from pluginsystem import object_feature_computation_plugin
import vigra
from vigra import numpy as np

class StandardObjectFeatures(object_feature_computation_plugin.ObjectFeatureComputationPlugin):
    """
    Computes the standard vigra region features
    """
    worksForDimensions = [2, 3]
    omittedFeatures = ["Global<Maximum >", "Global<Minimum >", 'Histogram', 'Weighted<RegionCenter>']

    def computeFeatures(self, rawImage, labelImage, frameNumber):
        return vigra.analysis.extractRegionFeatures(rawImage.astype('float32'),
                                                    labelImage.astype('uint32'),
                                                    ignoreLabel=0)

