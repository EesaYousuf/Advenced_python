# Custom Transformer Layer:
import torch
import torch.nn as nn
import torch.nn.functional as F
class CustomTransformerBlock(nn.Module):
    def __init__(self, embed_dim, heads):
        super().__init__()
        self.attn = nn.MultiheadAttention(embed_dim, heads)
        self.ff = nn.Sequential(
            nn.Linear(embed_dim, embed_dim * 4),
            nn.ReLU(),
            nn.Linear(embed_dim * 4, embed_dim)
        )
        self.norm1 = nn.LayerNorm(embed_dim)
        self.norm2 = nn.LayerNorm(embed_dim)
