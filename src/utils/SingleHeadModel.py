from torch.nn import Module, Sequential, Linear, LeakyReLU, Sigmoid

class SingleHeadModel(Module):
    def __init__(self, feature_count:int, hidden_count:int=5):
        super(SingleHeadModel, self).__init__()

        self.slope = 0.001

        self.model = Sequential(
            *[self.linear_block(feature_count,feature_count) for _ in range(hidden_count)],
            Linear(in_features=feature_count, out_features=1),
            Sigmoid()
        )

    def linear_block(self, in_features, out_features):
        return Sequential(
            Linear(in_features=in_features, out_features=out_features),
            LeakyReLU(negative_slope=self.slope)
        )
    
    def forward(self, x):
        return self.model(x)
